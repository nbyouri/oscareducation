# coding=utf-8
import random
import turtle

from examinations.models import *
import yaml

from questions_factory.models.problem_form import *
from questions_factory.models.problem_model import *
from collections import OrderedDict
import random

from skills.models import Skill

from questions_factory.models import *


# def triangle_draw():
#     def draw_triangle():
#         window = turtle.Screen()
#         window.bgcolor("green")  # background color
#         tom = turtle.Turtle()
#         tom.forward(100)
#         tom.forward(100)
#         tom.left(120)
#         tom.forward(100)
#         # window.exitonclick()  # to exit
#
#         tom.left(120)
#         # draw_triangle()


class TrianglePerimeterProblem(ProblemModel):

    def __init__(self, unit):
        ProblemModel.__init__(self)
        if unit != "m"  and unit != "dm" and unit != "cm"  and unit != "mm":
            raise ValueError
        self.unit = unit
        self.side_a = None
        self.side_b = None
        self.side_c = None

    def get_desc(self):
        pass

    def get_sol(self):
        return self.side_a + self.side_b + self.side_c

    def make_form(post_values):
        return TrianglePerimeterForm(post_values)

    def gen_questions(self, number_of_questions):
        questions = list()
        for _ in range(number_of_questions):
            questions.append((self.new_question(self.get_sol())))
            self.gen_values()
        return questions

    def new_question(self, sol):
        question_desc = "Quel est le périmètre d'un triangle de coté:" +str(self.side_a) + "," + str(self.side_b)+\
                        "and"+ str(self.side_c) + str(self.unit)
        #TODO METTRE EN PLUS LISIBLE

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
        #TODO DESC AND ID
        description = "Calculer le périmètre d'un triangle"
        skill_id = "T5-U5-A1b"
        default_context = Context.objects.create(
            file_name="generated",
            skill=Skill.objects.get(code=skill_id),
            context=description,
            added_by=None
        )
        return default_context

    def gen_values(self):
        self.side_a = random.randint(1.0, 9.0)
        self.side_b = random.randint(1.0, 9.0)
        self.side_c = random.randint(1.0, self.side_a + self.side_b -1.0)

