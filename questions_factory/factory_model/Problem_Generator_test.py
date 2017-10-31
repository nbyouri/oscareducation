import unittest
import json
import numpy

import os
from hamcrest import *
from Problem_Generator import *


class MyTestCase(unittest.TestCase):
############ Test normal behaviour ##############
    def test_get_solution_integer_rational_problem(self):
        val = [1, -3, 2]
        problem = create_problem("Integer", "Rational", val)
        [x_1, x_2] = problem.getSol()
        assert_that(2, equal_to(x_1))
        assert_that(1, equal_to(x_2))

    def test_get_val_integer_rational_problem(self):
        val = [1, -3, 2]
        problem = create_problem("Integer", "Rational", val)
        assert_that([1, -3, 2], equal_to(problem.getVal()))

    def test_gen_val_integer_rational_problem(self):
        problem = create_problem()
        val = problem.getVal()
        ans = numpy.roots(val)
        assert_that(ans.tolist(), contains(problem.getSol()))

    def test_get_solution_with_complex_range(self):
        problem = create_problem("Rational", "Rational", [1, 1, 20])
        assert_that([[]], contains(problem.getSol()))



########UTILS#######
def new_arithmetic_dict():
    dict = {}
    dict["problem"] = "Arithmetic_Polynomial_Second_degree"
    dict["desc"] = "blabla"
    return dict


def write_json_file(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def read_json_file():
    with open('json_tmp.txt') as json_file:
        return json_file


def remove_json_file(path):
    try:
        os.remove('json_tmp.txt')
    except:
        OSError("File doesn't exist")


def create_problem(domain= "Integer", range="Rational", val= None):
    json_path = 'json_tmp.txt'
    remove_json_file(json_path)
    dict = new_arithmetic_dict()
    dict["domain"] = domain
    dict["range"] = range
    if val:
        dict["val"] = val
    write_json_file(dict, json_path)
    problem = Problem_generator.factory(json_path)
    return problem


if __name__ == '__main__':
    unittest.main()
    remove_json_file("json_tmp.txt")
