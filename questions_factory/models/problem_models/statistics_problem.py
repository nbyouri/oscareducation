# coding=utf-8
import random

from questions_factory.models import Problem


class StatisticsProblem(Problem) :
    def __init__(self, range=(0, 20)):
        self.range = range
        self.values = None


    def gen_values(self):
        self.values = random.sample(range, 10)

