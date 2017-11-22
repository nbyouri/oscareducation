from questions_factory.models.problem_models.arithmetic_problem import *
from questions_factory.models.problem_models.simple_interest_problem import *


class ProblemGenerator:

    def __init__(self):
        pass

    def factory(input_dict):
        problem = input_dict["generator_name"]
        if problem == "ArithmeticProblem":
            domain, range, image = input_dict.pop("domain"), input_dict.pop("range"), input_dict.pop("image")
            values = input_dict.pop("val", None)
            return ArithmeticPolynomialSecondDegree(domain, image, range, values)
        elif problem == "SimpleInterestProblem":
            time_placed, type_rate = input_dict.pop("time_placed"), input_dict.pop("type_rate")
            return SimpleInterestProblem(time_placed, type_rate)
        else:
            raise ValueError('Wrong problem type')

    factory = staticmethod(factory)
