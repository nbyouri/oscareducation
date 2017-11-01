from django.test import TestCase
from .models import *
import json
import numpy
import os
from hamcrest import *


class NormalBehaviour(TestCase):
    def test_get_solution_integer_rational_problem(self):
        val = [1, -3, 2]
        problem = create_problem("Integer", "Rational", val)
        [x_1, x_2] = problem.get_sol()
        assert_that(2, equal_to(x_1))
        assert_that(1, equal_to(x_2))

    def test_get_val_integer_rational_problem(self):
        val = [1, -3, 2]
        problem = create_problem("Integer", "Rational", val)
        assert_that([1, -3, 2], equal_to(problem.get_val()))

    def test_get_solution_random_val_integer_complex_problem(self):
        problem = create_problem("Integer", "Complex")
        val = problem.get_val()
        ans = numpy.roots(val)
        assert_that([round(ans.tolist())], contains(problem.get_sol()))

    def test_get_solution_with_rational_range(self):
        problem = create_problem("Rational", "Rational", [1, 1, 20])
        assert_that([[]], contains(problem.get_sol()))


# TODO: Test unexpected behavior


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


def remove_json_file(file):
    try:
        os.remove(file)
    except:
        OSError("File doesn't exist")


def create_problem(domain="Integer", range="Rational", val=None):
    json_file = 'json_tmp.txt'
    remove_json_file(json_file)
    dict = new_arithmetic_dict()
    dict["domain"] = domain
    dict["range"] = range
    if val:
        dict["val"] = val
    write_json_file(dict, json_file)
    problem = Problem_generator.factory(json_file)
    remove_json_file(json_file)
    return problem


def round(list):
    new_list = []
    for x in list:
        if isinstance(x, complex):
            new_list.append(complex("{0:.2f}".format(x)))
        elif isinstance(x, float):
            new_list.append(float("{0:.2f}".format(x)))
    return new_list
