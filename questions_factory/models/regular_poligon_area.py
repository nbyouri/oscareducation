import math, random


def gen_values(self):
    self.s_lenght = None
    self.number_side = None


class RegularPoligonArea:
    def __init__(self):
        pass

    def gen_values(self):
        pass

    def get_desc(self):
        pass

    def get_sol(self):
        pass

    def make_form(self):
        pass


def area(self):
    Area = self.number_side * (math.pow(self.s_lenght, 2)) / (4 * math.tan(math.pi / self.number_side))
    print"nSide ", self.number_side, " lenght ", self.s_lenght, " area ", Area
    return Area


def gen_values(self):
    self.s_lenght = random(5, 10)
    self.number_side = random(1, 10)
