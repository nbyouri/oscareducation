import random
import turtle

from questions_factory.models import *


def triangle_draw():
    def draw_triangle():
        window = turtle.Screen()
        window.bgcolor("green")  # background color
        tom = turtle.Turtle()
        tom.forward(100)
        tom.forward(100)
        tom.left(120)
        tom.forward(100)
        # window.exitonclick()  # to exit

        tom.left(120)
        # draw_triangle()


class TrianglePerimeterProblem:
    def gen_values(self):
        pass

    def get_desc(self):
        pass

    def get_sol(self):
        pass

    def make_form(self):
        pass

    def __init__(self):
        sides = self.init_sides()
        self.side_a = sides[0]
        self.side_b = sides[1]
        self.side_c = sides[2]

    def init_sides(self):
        side_a = random.randint(1.0, 9.0)
        side_c = random.randint(1.0, 9.0)
        side_b = random.randint(1.0, 9.0)
        if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
            return [side_a, side_b, side_c]
        return self.init_sides()

    def calculate_perimeter(self):
        p = self.init_sides()
        return p[0] + p[1] + p[2]
