from problem_model import *
import random
import numpy


class Arithmetic_polynomial_second_degree(Problem_model):
    def __init__(self, domain, range, val=None):
        Problem_model.__init__(self, "Polynomial second degree", domain, range)
        if val and len(val) == 3:
            self.val = val
        else:
            self.genNewValues()

    def genNewValues(self):
        self.val = list()
        self.genValues()

    def genValues(self):
        if (self.domain == "Natural"):
            for i in range(3):
                self.val.append(random.randint(0, 100)) #TODO What range should we put ?
        elif (self.domain == "Integer"):
            for i in range(3):
                self.val.append(random.randint(-100, 100))
        elif (self.domain == "Rational"):
            for i in range(3):
                self.val.append(random.uniform(-100, 100))
        else:
            raise ValueError("Wrong value for domain: ",self.domain)

    def getDesc(self):
        return self.desc

    def getVal(self):
        return self.val

    def round(self, list):
        new_list = []
        for x in list:
            if isinstance(x, complex):
                new_list.append(complex("{0:.2f}".format(x)))
            elif isinstance(x, float):
                new_list.append(float("{0:.2f}".format(x)))
        return new_list

    def getSol(self):
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
            raise ValueError("Wrong value for range:",self.range)

        return self.round(sol)
