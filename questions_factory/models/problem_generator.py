from arithmetic_problem import *
from simple_interest_problem import *
import json


class ProblemGenerator:

    def __init__(self):
        pass

    def factory(json_i):
        global problem, domain, image, range, values
        input = json.loads(json_i)
        problem = input["problem"]
        if problem == "Arithmetic_Polynomial_Second_degree":
            domain, range, image = input.pop("domain"), input.pop("range"), input.pop("image")
            values = input.pop("val", None)
            return ArithmeticPolynomialSecondDegree(domain, image, range, values)
        elif problem == "Simple_Interest_Problem":
            time_placed, type_rate = input.pop("time_placed"), input.pop("type_rate")
            return SimpleInterestProblem(time_placed, type_rate)
        else:
            raise ValueError('Wrong problem type')

    factory = staticmethod(factory)
