# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import yaml
import yamlordereddictloader
import json


class Context(models.Model):
    """[FR] Contexte, Exercice

        Contains a list of Questions (at least one).
        A Context is also called an exercise/exercice
        in the code comments or in the documentation.

    """

    context = models.TextField(blank=True, null=True)
    """The general description related to the Question(s), not mandatory."""
    skill = models.ForeignKey("skills.Skill")
    """The Skill evaluated through this Context"""

    added_by = models.ForeignKey(User, null=True)
    """The Professor who created this Context and its Question(s)"""
    # TODO: added_by must be NOT NULL

    approved = models.BooleanField(default=True)
    """True if in a correct format, False otherwise"""
    created_at = models.DateTimeField(auto_now_add=True)
    """Date of creation"""
    modified_at = models.DateTimeField(auto_now=True)
    """Date of the last modification"""
    testable_online = models.BooleanField(default=True)
    """True if can be graded automatically, False otherwise"""
    file_name = models.CharField(max_length=255, null=True, blank=True)
    """\"submitted\" if created online, \"adapted\" if modified for a Test,
        \"a_file_name\" if the exercise is stored in a file (method not used anymore)"""

    def get_questions(self):
        """Get all the questions attached to this Context."""
        list_questions = list()
        questions = list()
        for list_question in List_question.objects.filter(context=self.id):
            list_questions.append(list_question.question.id)
        for question in Question.objects.filter(id__in=list_questions):
            questions.append(question)
        return questions


class List_question(models.Model):
    """List of questions

        Link between Contexts and Questions.

    """

    context = models.ForeignKey('Context')
    """A Context"""
    question = models.ForeignKey('Question')
    """A Question"""


class Question(models.Model):
    """[FR] Question

        Represents a Question, that must belong
        to a Context.

    """
    # @todo after migration add type question filed from answer yaml structure

    description = models.TextField(blank=True, null=True)
    """The description is where states the question itself"""
    answer = models.TextField()
    """The list of possible true answers, as well as false answers, depending on the type.
        For now, the type is also included in this field."""
    source = models.CharField(max_length=255, null=True, blank=True)
    """Information that can only the Professors"""

    def get_answer(self):
        # Load YAML answer
        if self.answer:
            return yaml.load(self.answer, Loader=yamlordereddictloader.Loader)

        return {}

    def get_type(self):
        yaml_answer = self.get_answer()
        return yaml_answer["type"]

    def get_answers(self):
        yaml_answer = self.get_answer()
        return yaml_answer["answers"]

    def get_answers_extracted(self):
        print(type(self.get_answers().items()))
        return self.get_answers().items()

    def get_graph_points(self):
        coordinates = list()
        yaml_answer = self.get_answers()
        for points in yaml_answer:
            x = points["graph"]["coordinates"]["X"]
            y = points["graph"]["coordinates"]["Y"]
            coordinates.append((x, y))
        return coordinates

    def evaluate(self, response):
        """Evaluates this Question with the provided response

            :param response: The response to assess
            :type response: array
            :returns: 1 if the response is correct, 0 if incorrect, -1 if automatic evaluation is impossible
            :rtype: int
            """
        raw_correct_answers = self.get_answer()
        evaluation_type = raw_correct_answers["type"]

        if evaluation_type == "text":
            # We only need the first and only element: the text by the Student
            response = response[0]
            if isinstance(response, (int, float)):
                response = str(response)

            correct_answers = [unicode(x).lower().strip().replace(" ", "").encode('UTF-8')
                               for x in raw_correct_answers["answers"]]
            response = response.strip().replace(" ", "").lower().encode("Utf-8") if isinstance(response,
                                                                                           basestring) else response

            if response in [x for x in correct_answers]:
                return 1
            else:
                return 0

        elif evaluation_type.startswith("math"):
            # We only need the first and only element: the math formula by the Student
            response = response[0]

            correct_answers = [unicode(x).lower().strip().replace(" ", "").encode("Utf-8")
                               for x in raw_correct_answers["answers"]]
            response = response.strip().replace(" ", "").lower().encode("Utf-8") if isinstance(response,
                                                                                               basestring) else response

            if response in [x for x in correct_answers]:
                return 1
            else:
                return 0

        elif evaluation_type == "radio":
            # We only need the first and only element: the answer selected by the Student
            response = response[0]

            # The list of correct/incorrect answers
            answers = raw_correct_answers["answers"]

            # If no selected answer
            if response == -1:
                return 0
            # If the selected answer is not part of the list, should not be possible for a Student
            elif response > len(raw_correct_answers.values()):
                return 0
            # If the selected answer is True (correct)
            elif answers.values()[response]:
                return 1
            # Else, a false answer has been selected by the Student
            else:
                return 0

        elif evaluation_type == "graph":
            """
            result_answer["answers"] = []
            points_student_answers = []
            points_good_answers = []

            # first we need to get all student answer and all good answers
            for subnumber, graph_answers in enumerate(raw_correct_answers["answers"]):
                if graph_answers["graph"]["type"] == "point":
                    X = answers.get("graph-%s-point-%s-X" % (number, subnumber), "")
                    Y = answers.get("graph-%s-point-%s-Y" % (number, subnumber), "")

                    X = int(X) if X.isdigit() else None
                    Y = int(Y) if Y.isdigit() else None

                    points_student_answers.append({"X": X, "Y": Y})
                    points_good_answers.append(graph_answers["graph"]["coordinates"])
                else:
                    assert False

            # now we need to see if the student answers are in the good answers
            for point in points_student_answers:
                print point
                result_answer["answers"].append({
                    "answer": point,
                    "correct": True,
                    "type": "point",
                })
                if point not in points_good_answers:
                    result_answer["answers"][-1]["correct"] = False
                    result_answer["answers"][-1]["correct_answer"] = None
                else:
                    points_good_answers.remove(point)
                    result_answer["answers"][-1]["correct_answer"] = point

            # and for all bad answers lets put a correct answer next to it
            for i in result_answer["answers"]:
                if i["correct_answer"] is None:
                    i["correct_answer"] = points_good_answers.pop()

            result_answer["correct"] = all([x["correct"] for x in result_answer["answers"]])
            """
            return 0

        elif evaluation_type == "checkbox":
            # The list of correct/incorrect answers
            answers = raw_correct_answers["answers"]

            for checkbox_number, is_correct in enumerate(answers.values()):
                if is_correct and checkbox_number not in response:
                    return 0
                if not is_correct and checkbox_number in response:
                    return 0
            # All the correct answers are selected, all the incorrect ones not selected
            return 1

        elif evaluation_type == "professor":
            # No automatic verification to perform if corrected by a Professor
            return -1

        # No automatic correction type found, not corrected by default
        else:
            return -1


class Answer(models.Model):
    """[FR] Réponses

        The answers from a student, through a test,
        corresponding to Contexts (of Question(s))
        that belong to that test

    """

    raw_answer = JSONField(null=True, blank=True)  # let's store json
    """The answers the student provided to all the Question(s) belonging to a Context"""
    from_test_hybride = models.BooleanField(default=False)
    """Depreciated"""
    automatic = models.BooleanField(default=False)
    """If we already succeed in a Context which the Skill used our Context Skill as prerequisite,
        we automatically succeed to answer to this Context, whatever our raw_answer was"""
    test_student = models.ForeignKey("TestStudent")
    """The TestStudent (the test itself) corresponding to our answers"""
    test_exercice = models.ForeignKey("TestExercice")
    """The TestExercice (which Context in the test) corresponding to our answers"""
    answer_datetime = models.DateTimeField(auto_now_add=True)
    """The date we submitted our answers"""

    def get_questions_with_answers(self):
        questions_with_answers = list()
        index = 0
        for question in self.test_exercice.exercice.get_questions():
            questions_with_answers.append(
                [index,
                 question,
                 question.get_type(),
                 self.get_answers()[str(index)].get("response"),
                 self.get_answers()[str(index)].get("correct")
                 ])
            index += 1
        return questions_with_answers

    def contains_professor(self):
        """Does the Answer contain a response that need to be assessed by a Professor?

        :return: True if the Answer has at least one response of Professor type, False otherwise
        :rtype: bool
        """
        professor = False
        for question in self.test_exercice.exercice.get_questions():
            if question.get_type() == "professor":
                professor = True
        return professor

    def assess(self, index, correction):
        """Grades manually an answer to a question

        :param index: The question index to be corrected
        :type index: int
        :param correction: The correction value : 1 if correct, 0 if incorrect
        :type correction: int
        :return: True if the correction is useful, False if it does not change the grade
        :rtype: bool
        """
        answers = self.get_answers()
        # No need to correct
        if answers[str(index)]["correct"] == correction:
            return False
        else:
            answers[str(index)]["correct"] = correction
            return True

    def evaluate(self):
        """Evaluates the attached Context, determines if all of its Questions are correct

            :return: -1 if no all questions are graded, 1 if all the answers to the Questions are correct,
                    0 if there is at least a mistake
            :rtype: int
            """
        result = 1
        for question in json.loads(self.raw_answer)[0].values():
            if question["correct"] == -1:
                return -1
            elif question["correct"] != 1:
                result = 0
        return result

    def get_answers(self):
        return json.loads(self.raw_answer)[0]

    def get_answers_extracted(self):
        return json.loads(self.raw_answer)[0]


class TestStudent(models.Model):
    """A student test

        The Test of a particular Student.

    """
    student = models.ForeignKey("users.Student")
    """The Student"""
    test = models.ForeignKey("Test")
    """The Test"""
    finished = models.BooleanField(default=False)
    """True if the Student has finished the Test, False otherwise"""
    started_at = models.DateTimeField(null=True)
    """The date the Student started the Test"""
    finished_at = models.DateTimeField(null=True)
    """The date the Student finished the Test"""

    class Meta:
        ordering = ['test__created_at']

    def test_exercice_answer_for_offline_test(self):
        answers = {x.test_exercice: x for x in self.answer_set.all().select_related("test_exercice")}

        return [(x, answers.get(x)) for x in
                TestExercice.objects.filter(test=self.test, testable_online=False, exercice__isnull=False)]

    def has_offline_answers(self):
        return self.answer_set.filter(test_exercice__testable_online=False).exists()

    def get_maybe_answer_list(self):
        answers = {x.test_exercice: x for x in
                   self.answer_set.all().select_related("test_exercice").order_by("-test_exercice__skill__code")}

        return [answers.get(x) for x in TestExercice.objects.filter(test=self.test).order_by("-skill__code")]

    def get_state(self):
        if not self.started_at:
            return u"pas encore commencé"
        elif not self.finished_at:
            return u"commencé"
        else:
            return u"fini"

    def __unicode__(self):
        return u"on %s (%s)" % (self.student, self.get_state())


class TestExercice(models.Model):
    """A test context

        Represents the link between a Test and its Context(s)
        of Question(s).

    """
    test = models.ForeignKey("Test")
    """The Test"""
    exercice = models.ForeignKey("Context", null=True)
    """A Context that belongs to the Test"""
    skill = models.ForeignKey("skills.Skill")
    """The Skill of the Context, necessary in case there is no Context ready
        for this Skill"""
    created_at = models.DateTimeField(auto_now_add=True)
    """The date the Context was added to the Test"""
    variables = models.TextField(null=True, blank=True)
    """Unused field"""
    rendered_content = models.TextField(null=True, blank=True)
    """Unused field"""
    testable_online = models.BooleanField(default=True)
    """True if this Context is graded automatically, False otherwise"""

    def is_valid(self, answers):
        """Verifies if the answers are correct, if they can be graded automatically"""
        return self.exercice.check_answers(answers)["is_valid"]


class BaseTest(models.Model):
    """Base for the Tests

        This is the common part of the Tests,
        whether "classic" or offline

    """
    name = models.CharField(max_length=255, verbose_name="Nom")
    """The test name"""
    lesson = models.ForeignKey("promotions.Lesson")
    """The Lesson in which this test stands"""
    skills = models.ManyToManyField("skills.Skill")
    """The Skill(s) tested in this test"""
    created_at = models.DateTimeField(auto_now_add=True)
    """The date the test was created"""


class Test(BaseTest):
    """[FR] Test

        A test created with Oscar, linked with
        a suite of Contexts, to evaluate a Student.

    """
    running = models.BooleanField(default=True)
    """True while it is open (available for students), becomes False when closed by the Professor"""
    enabled = models.BooleanField(default=True)
    """True if the test is visible, False if invisible (not to confuse with "running")"""
    fully_testable_online = models.BooleanField(default=True)
    """True if all the Contexts in the Test can be graded automatically"""

    type = models.CharField(max_length=255, choices=(
        ("skills", "skills"),
        ("dependencies", "dependencies"),
        ("skills-dependencies", "skills-dependencies"),
    ))
    """The type test: it can test the Skills themselves, their prerequisites, or both"""

    def can_change_exercice(self):
        # None of the students has started its test yet.
        return not self.teststudent_set.filter(started_at__isnull=False).exists()

    def add_student(self, student):
        """ subscribe new student in prof created tests """

        TestStudent.objects.create(
            test=self,
            student=student
        )

    def testexercice_with_skills(self):
        return self.testexercice_set.select_related("skill").order_by('-skill__code')

    def teststudent_with_student(self):
        return self.teststudent_set.select_related("student", "student__user")

    def testexercice_testable_online(self):
        return self.testexercice_set.filter(testable_online=True).select_related("skill")

    def testexercice_testable_offline(self):
        return self.testexercice_set.filter(testable_online=False, exercice__isnull=False).select_related("skill")

    def display_test_type(self):
        if self.type == "skills":
            return "compétences"
        if self.type == "dependencies":
            return "prérequis"
        if self.type == "skills-dependencies":
            return "compétences et prérequis"

    def generate_skills_test(self):
        for skill in self.skills.all():
            TestExercice.objects.create(
                test=self,
                skill=skill,
            )

    def generate_dependencies_test(self):
        to_test_skills = []

        def recursivly_get_skills_to_test(skill):
            for i in skill.depends_on.all():
                if i not in to_test_skills:
                    to_test_skills.append(i)
                    recursivly_get_skills_to_test(i)

        for skill in self.skills.all():
            recursivly_get_skills_to_test(skill)

        for skill in to_test_skills:
            TestExercice.objects.create(
                test=self,
                skill=skill,
            )

    def generate_skills_dependencies_test(self):
        to_test_skills = []

        def recursivly_get_skills_to_test(skill):
            for i in skill.depends_on.all():
                # we don't add dependancies that can't be tested online
                if i not in to_test_skills and skill.exercice_set.filter(testable_online=True).exists():
                    to_test_skills.append(i)
                    recursivly_get_skills_to_test(i)

        for skill in self.skills.all():
            recursivly_get_skills_to_test(skill)

            TestExercice.objects.create(
                test=self,
                skill=skill,
            )

        for skill in to_test_skills:
            if TestExercice.objects.filter(skill=skill, test=self).exists():
                continue

            TestExercice.objects.create(
                test=self,
                skill=skill,
            )

    def __unicode__(self):
        return self.name


class TestFromClass(BaseTest):
    """[FR] Test hors-ligne

        This test is done in class, not with Oscar.
        Its purpose is to encode the results online.

    """
    pass


class TestSkillFromClass(models.Model):
    """[FR] Compétence de test hors-ligne

        This is the link between a TestFromClass
        and its Skill(s)

    """
    test = models.ForeignKey("TestFromClass")
    """The offline Test"""
    skill = models.ForeignKey("skills.Skill")
    """A Skill tested by the offline Test"""
    student = models.ForeignKey("users.Student")
    """The student that passed the offline Test"""
    result = models.CharField(max_length=10, choices=(
        ("good", "acquise"),
        ("bad", "non acquise"),
        ("unknown", "inconnu"),
    ))
    """The Skill result for the Student with the offline Test"""

    created_at = models.DateTimeField(auto_now_add=True)