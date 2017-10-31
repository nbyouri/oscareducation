from Problem_Model import *
import random
import numpy


class Arithmetic_polynomial_second_degree(Problem_model):
    def __init__(self, desc, domain, range, val=None):
        Problem_model.__init__(self, desc, domain, range)
        if val:
            self.val = val  # TODO Check if values correspond to domain and right number of values
        else:
            self.genNewValues()

    def genNewValues(self):
        self.val = list()
        self.genValues()

    def genValues(self):
        if (self.domain == "Natural"):
            for i in range(3):
                self.val.append(random.randint(0, 100))
        elif (self.domain == "Integer"):
            for i in range(3):
                self.val.append(random.randint(-100, 100))
        elif (self.domain == "Rational"):
            for i in range(3):
                self.val.append(random.uniform(-100, 100))
        else:
            raise ValueError("Wrong Domain")

    def getDesc(self):
        return self.desc

    def getVal(self):
        return self.val

    def getSol(self):
        tmp_sol = numpy.roots(self.val)
        sol = tmp_sol
        #if (self.range == "Rational"):
        #    for root in tmp_sol:
        #        if root.iscomplex():
        #            numpy.delete(sol, root)
        return sol
