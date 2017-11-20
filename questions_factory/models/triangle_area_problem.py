import math
import turtle, random
from cmath import sqrt
from decimal import Decimal

import screen as screen

from questions_factory.models import *
from questions_factory.models.triangle_draw import TriangleDraw, draw_triangle


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
        draw_triangle(self) # ABSOLUTELY FLOAT!
        if (self.side_a + self.side_b > self.side_c) and (self.side_a + self.side_c > self.side_b) and (self.side_b + self.side_c > self.side_a):
            s = self.side_a + self.side_b + self.side_c
            s = s / 2.0
            print"s->", s
            print"side_a->", self.side_a
            print"side_b->", self.side_b
            print"side_c->", self.side_c
            output1 = Decimal(math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)))  # erone method for area
            output2 = round(output1, 2)
            return output2

        else:
            self.area()

