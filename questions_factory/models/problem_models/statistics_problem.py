# coding=utf-8
import random
import numpy
import yaml

from collections import OrderedDict
from examinations.models import *
from questions_factory.models.problem_form import *
from questions_factory.models.problem_models.problem import *


class StatisticsProblem(Problem) :
    def __init__(self, nb=10, range=(0, 20)):
        self.range = range
        self.values = None
        self.nb = nb
        self.gen_values()

    def gen_values(self):
        self.values = random.sample(self.range, self.nb)


    def get_sol(self):
        sol = list()
        average = self.get_average()
        sol.append(average)
        median = self.get_median()
        sol.append(median)
        standard_deviation = self.get_standard_deviation()
        sol.append(standard_deviation)


    def gen_questions(self, number_of_questions):
        questions = list()
        for _ in range(number_of_questions):
            questions.append((self.new_question(self.get_sol())))
            self.gen_values()
        return questions

    def new_question(self, sol):
        question_desc = "Voici une série de données recueillies pour chaque jour écoulée durant" + str(self.nb) + " jours : "
        + str(self.values)
        answers = yaml.dump(OrderedDict([("answers", [sol]), ("type", "text")]))
        question = Question(description=question_desc, answer=answers, source="Génerée automatiquement")
        return question

    @staticmethod
    def make_form(post_values):
        return StatisticsForm(post_values)


    def get_average(self):
        m = numpy.mean(self.values)
        return m

    def get_median(self):
        m = numpy.median(self.values)
        return m

    def get_standard_deviation(self):
        sd = numpy.std(self.values)
        return sd

