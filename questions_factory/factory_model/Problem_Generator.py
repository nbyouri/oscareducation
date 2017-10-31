from Arithmetic_Problem import *
import json


class Problem_generator:
    def factory(json_path):
        global problem, desc, domain, range, values
        with open(json_path) as json_file:
            input = json.load(json_file)
        try:
            problem, desc = input.pop("problem"), input.pop("desc")
            domain, range = input.pop("domain"), input.pop("range")
            val = input.pop("val", None)
        except:
            KeyError()

        if problem == "Arithmetic_Polynomial_Second_degree":
            return Arithmetic_polynomial_second_degree(desc, domain, range, val)
        else:
            raise ValueError
    factory = staticmethod(factory)