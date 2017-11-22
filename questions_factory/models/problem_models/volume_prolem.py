# coding=utf-8

from examinations.models import *
import yaml

from oscar.settings import STATIC_URL
from questions_factory.models.problem_form import *
from questions_factory.models.problem_models.problem import *
from collections import OrderedDict
import random
import math

from skills.models import Skill


class VolumeProblem(Problem):
    default_cube = ('cote (a)', 1)
    default_cylinder = [('rayon de la base (r)', 1), ('hauteur (h)', 2)]
    default_prism = [('base (b)', 1), ('hauteur de la base (h)', 1), ('hauteur (l)', 2)]
    default_cone = [('rayon de la base (r)', 1), ('hauteur (h)', 2)]
    default_pyramid = [('longueur de la base (l)', 1), ('largeur de la base (w)', 1), ('hauteur (h)', 2)]
    object_type = None
    object_name = None

    def __init__(self, object_type):
        Problem.__init__(self)
        if object_type != 'cube'            \
            and object_type != 'cylinder'   \
            and object_type != 'prism'      \
            and object_type != 'cone'       \
                and object_type != 'pyramid':
                raise ValueError
        self.object_type = object_type
        self.figure = None
        self.gen_values()

    def gen_values(self):
        # form to specify XXX
        # round values XXX
        # units XXX
        scale_base_length = random.randint(0, 100)
        scale_base_width = random.randint(0, 100)
        scale_height = random.randint(0, 100)

        if self.object_type == 'cube':
            self.object_name = 'du cube'
            self.figure = [(self.default_cube[0], scale_base_length * self.default_cube[1])]
        elif self.object_type == 'cylinder':
            self.object_name = 'du cylindre'
            self.figure = [(self.default_cylinder[0][0], self.default_cylinder[0][1] * scale_base_length),  # radius
                           (self.default_cylinder[1][0], self.default_cylinder[1][1] * scale_height)]
        elif self.object_type == 'prism':
            self.object_name = 'du prisme'
            self.figure = [(self.default_prism[0][0], self.default_prism[0][1] * scale_base_length),
                           (self.default_prism[1][0], self.default_prism[1][1] * scale_base_width),  # triangle height
                           (self.default_prism[2][0], self.default_prism[2][1] * scale_height)]
        elif self.object_type == 'cone':
            self.object_name = 'du cone'
            self.figure = [(self.default_cone[0][0], self.default_cone[0][1] * scale_base_length),  # radius
                           (self.default_cone[1][0], self.default_cone[1][1] * scale_height)]
        elif self.object_type == 'pyramid':
            self.object_name = 'de la pyramide'
            self.figure = [(self.default_pyramid[0][0], self.default_pyramid[0][1] * scale_base_length),
                           (self.default_pyramid[1][0], self.default_pyramid[1][1] * scale_base_width),
                           (self.default_pyramid[2][0], self.default_pyramid[2][1] * scale_height)]
        else:
            raise ValueError

    @staticmethod
    def make_form(post_values):
        return VolumeProblemForm(post_values)

    def get_desc(self):
        pass

    def get_sol(self):
        if self.object_type == 'cube':
            return pow(self.figure[0][1], 3)
        elif self.object_type == 'cylinder':
            return math.pi * pow(self.figure[0][1], 2) * self.figure[1][1]
        elif self.object_type == 'prism':
            return 0.5 * self.figure[0][1] * self.figure[1][1] * self.figure[2][1]
        elif self.object_type == 'cone':
            return math.pi * pow(self.figure[0][1], 2) * (self.figure[1][1] / 3)
        elif self.object_type == 'pyramid':
            return (self.figure[0][1] * self.figure[1][1] * self.figure[2][1]) / 3
        else:
            raise ValueError

    def gen_questions(self, number_of_questions):
        questions = list()
        for _ in range(number_of_questions):
            questions.append((self.new_question(self.get_sol())))
            self.gen_values()
        return questions

    def new_question(self, sol):
        question_desc = '<img src=\"' + str(STATIC_URL) + 'img/Figures/' + self.object_type + '.png\" /><br>'
        question_desc += 'Calculer le volume ' + self.object_name + ' dont les parametres sont:<ul>'
        for e in self.figure:
            question_desc += '<br><li>%s = %s</li>' % (e[0], e[1])
        question_desc += '</ul>'
        answers = yaml.dump(OrderedDict([("answers", [sol]), ("type", "text")]))
        question = Question(description=question_desc, answer=answers, source="Génerée automatiquement")
        return question

    def get_context(self):
        default_context = self.default_context()
        # TODO Get from db if already Context already exist
        # context, created = Context.objects.get_or_create(defaults=default_context, file_name="generated")
        return default_context

    @staticmethod
    def default_context():
        description = "Calcul de volume dans des figures en trois dimensions"
        skill_id = "T4-U5-A1b" # ??
        default_context = Context.objects.create(
            file_name="generated",
            skill=Skill.objects.get(code=skill_id),
            context=description,
            added_by=None
        )
        return default_context
