from arithmetic_problem import *
import json


class Problem_generator:

    def factory(json_i):
        global problem, domain, range, values
        input = json.loads(json_i)
        try:
            problem = input["problem"]
            domain, range = input.pop("domain"), input.pop("range")
            values = input.pop("val", None)
        except:
            KeyError()

        if problem == "Arithmetic_Polynomial_Second_degree":
            return Arithmetic_polynomial_second_degree(domain, range, values)
        else:
            raise ValueError
    factory = staticmethod(factory)