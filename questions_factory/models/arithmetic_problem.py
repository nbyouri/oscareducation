# coding=utf-8
from problem_model import *
import random
import numpy


class Arithmetic_polynomial_second_degree(Problem_model):
    def __init__(self, domain, image, range, val=None):
        Problem_model.__init__(self, "Polynomial second degree", domain, image, range)
        if val and len(val) == 3:
            self.val = val
        elif image == "Integer":
            self.gen_values_from_sol()
        else:
            self.gen_new_values()

    def gen_new_values(self):
        self.val = list()
        self.gen_values()

    def gen_values(self):
        if self.domain == "Natural":
            for i in range(3):
                self.val.append(random.randint(self.range[0], self.range[1]))  # TODO What range should we put ?
        elif self.domain == "Integer":
            for i in range(3):
                self.val.append(random.randint(self.range[0], self.range[1]))
        elif self.domain == "Rational":
            for i in range(3):
                self.val.append(random.uniform(self.range[0], self.range[1]))
        else:
            raise ValueError("Wrong value for domain: ", self.domain)

    def gen_values_from_sol(self):
        sol = [random.randint(-20, 20), random.randint(-20, 20)]
        sum, prod = sol[0] + sol[1], sol[0] * sol[1]
        # For polynom of type ax²+bx+c
        a = random.randint(-20, 20)
        b = -1*sum*a
        c = prod*a
        self.val = [a, b, c]

    def get_desc(self):
        return self.desc

    def get_val(self):
        return self.val

    @staticmethod
    def round(list):
        new_list = []
        for x in list:
            if isinstance(x, complex):
                new_list.append(complex("{0:.2f}".format(x)))
            elif isinstance(x, float):
                new_list.append(float("{0:.2f}".format(x)))
        return new_list

    def get_sol(self):
        tmp_sol = numpy.roots(self.val).tolist()
        sol = list()
        if self.image == "Rational" or self.image == "Integer":
            sol = list()
            for root in tmp_sol:
                if not isinstance(root, complex):
                    sol.append(root)
        elif self.image == "Complex":
            sol = tmp_sol
        else:
            raise ValueError("Wrong value for image:", self.image)

        return self.round(sol)

    def gen_questions(self, number_of_questions):
        questions = list()
        for _ in range(number_of_questions):
            # We only want problems having a solution
            while not self.get_sol():
                self.gen_new_values()
            questions.append((self.get_val(), self.get_sol()))
            self.gen_new_values()
        return questions
