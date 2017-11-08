import random
from cmath import sqrt

from questions_factory.models import *


class TriangleAreaProblem(TrianglePerimeterProblem):
    def gen_values(self):
        pass

    def get_desc(self):
        pass

    def get_sol(self):
        pass

    def make_form(self):
        pass

    def __init__(self):
        TrianglePerimeterProblem.__init__(self)
        sides = self.init_sides()
        self.side_a = sides[0]
        self.side_b = sides[1]
        self.side_c = sides[2]

    def area(self):
        p = self.init_sides() / 2.0
        return sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) # erone method

    def init_sides(self):
        side_a = random.randint(1, 9)
        side_c = random.randint(1, 9)
        side_b = random.randint(1, 9)
        if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
            return [side_a, side_b, side_c]
        return self.init_sides()
