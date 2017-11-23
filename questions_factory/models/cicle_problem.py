import turtle
import math

from questions_factory.models import *


def circle():
    radius =  random.randint(1.0, 9.0)


class CircleProblem():
    def gen_values(self):
        pass

    def get_desc(self):
        pass

    def get_sol(self):
        pass

    def make_form(self):
        pass

    def area(self):
        area = math.pow(self.radius, 2) * 3.14  # pi
        return area

    def draw_circle(self):
        window = turtle.Screen()
        window.bgcolor("blue")
        window.title("Triangle Right!")
        tur = turtle.Turtle()
        tur.color("green")
        tur.width(5)
        tur.circle(self.radius)
        window.exitonclick()
