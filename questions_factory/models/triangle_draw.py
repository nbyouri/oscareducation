import math
import turtle
from questions_factory.models import *

MOLT = 20


class TriangleDraw(TrianglePerimeterProblem):  # is all correct?
                                               # Doubts of how to acquire the side_a, side_b, side_c
                                               # Does it works as it should? We will see...
    def gen_values(self):
        pass

    def get_desc(self):
        pass

    def get_sol(self):
        pass

    def make_form(self):
        pass


def __init__(self):
    TriangleDraw.__init__(self)
    sides = self.init_sides()
    self.side_a = sides[0]
    self.side_b = sides[1]
    self.side_c = sides[2]


def draw_triangle(self):
    if self.side_a == self.side_b == self.side_c:
        draw_triangle_equilater(self.side_a, self.side_b, self.side_c)

    if round(math.pow(self.side_a, 2.0)) + round(math.pow(self.side_b, 2.0)) == round(math.pow(self.side_c, 2.0)) or round(math.pow(self.side_b, 2.0)) + round(
            math.pow(self.side_c, 2.0)) == round(math.pow(self.side_a, 2.0)) or round(math.pow(self.side_c, 2.0)) + round(math.pow(self.side_a, 2.0)) == round(
        math.pow(self.side_b, 2.0)):
        draw_triangle_90(self.side_a, self.side_b, self.side_c)
    else:
        draw_triangle_scalene(self.side_a, self.side_b, self.side_c)


def draw_triangle_90(a, b, c):
    window = turtle.Screen()
    window.bgcolor("purple")
    window.title("Triangle Right!")
    tur = turtle.Turtle()
    tur.color("yellow")
    tur.width(5)
    if round(math.pow(a, 2)) + round(math.pow(b, 2)) == round(math.pow(c, 2)):
        tur.forward(a * MOLT)
        tur.left(90)
        tur.forward(b * MOLT)
        rad = math.acos(b / c)
        ang = math.degrees(rad)
        tur.left(180 - ang)
        tur.forward(c * MOLT)
        window.exitonclick()

    if round(math.pow(b, 2)) + round(math.pow(c, 2)) == round(math.pow(a, 2)):
        tur.forward(b * MOLT)
        tur.left(90)
        tur.forward(c * MOLT)
        rad = math.acos(c / a)
        ang = math.degrees(rad)
        tur.left(180 - ang)
        tur.forward(a * MOLT)
        window.exitonclick()
    else:
        tur.forward(c * MOLT)
        tur.left(90)
        tur.forward(a * MOLT)
        rad = math.acos(a / b)
        ang = math.degrees(rad)
        # print " 3->", ang
        tur.left(180 - ang)
        tur.forward(b * MOLT)


def draw_triangle_scalene(a, b, c):
    window = turtle.Screen()
    window.bgcolor("purple")
    window.title("Triangle Scalene!")
    tur = turtle.Turtle()
    tur.color("yellow")
    tur.width(10)
    tur.forward(a * MOLT)
    rad = math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)
    rad = rad / 2
    rad = rad / a
    rad = rad / b
    rad = math.acos(rad)
    ang = math.degrees(rad)
    tur.left(180 - ang)
    tur.forward(b * MOLT)
    rad = math.pow(c, 2) + math.pow(b, 2) - math.pow(a, 2)
    rad = rad / 2
    rad = rad / c
    rad = rad / b
    rad = math.acos(rad)
    ang = math.degrees(rad)
    tur.left(180 - ang)
    tur.forward(c * MOLT)
    window.exitonclick()


def draw_triangle_equilater(a, b, c):
    window = turtle.Screen()
    window.bgcolor("purple")
    window.title("Triangle Equilater!")
    tur = turtle.Turtle()
    tur.color("yellow")
    tur.width(10)
    tur.forward(a * 100)
    tur.left(120)
    tur.forward(b * 100)
    tur.left(120)
    tur.forward(c * 100)
    window.exitonclick()
