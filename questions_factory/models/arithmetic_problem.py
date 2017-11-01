from problem_model import *
import random
import numpy


class Arithmetic_polynomial_second_degree(Problem_model):
    def __init__(self, domain, range, val=None):
        Problem_model.__init__(self, "Polynomial second degree", domain, range)
        if val and len(val) == 3:
            self.val = val
        else:
            self.gen_new_values()

    def gen_new_values(self):
        self.val = list()
        self.gen_values()

    def gen_values(self):
        if (self.domain == "Natural"):
            for i in range(3):
                self.val.append(random.randint(0, 100))  # TODO What range should we put ?
        elif (self.domain == "Integer"):
            for i in range(3):
                self.val.append(random.randint(-100, 100))
        elif (self.domain == "Rational"):
            for i in range(3):
                self.val.append(random.uniform(-100, 100))
        else:
            raise ValueError("Wrong value for domain: ", self.domain)

    def get_desc(self):
        return self.desc

    def get_val(self):
        return self.val

    def round(self, list):
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
        if (self.range == "Rational"):
            sol = list()
            for root in tmp_sol:
                if not isinstance(root, complex):
                    sol.append(root)
        elif (self.range == "Complex"):
            sol = tmp_sol
        else:
            raise ValueError("Wrong value for range:", self.range)

        return self.round(sol)

    def gen_questions(self, number_of_questions):
        values = list()
        solutions = list()
        questions = dict()
        for _ in range(number_of_questions):
            values.append(self.get_val())
            solutions.append(self.get_sol())
            self.gen_new_values()
        questions["values"] = values
        questions["solutions"] =  solutions
        return questions