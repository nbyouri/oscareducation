from django.test import TestCase
from .models import *
import json
import numpy
import os
from hamcrest import *


class NormalBehaviour(TestCase):
    @staticmethod
    def test_get_solution_integer_rational_problem():
        val = [1, -3, 2]
        problem = create_problem("Integer", "Rational", [0, 20], val)
        [x_1, x_2] = problem.get_sol()
        assert_that(2, equal_to(x_1))
        assert_that(1, equal_to(x_2))

    @staticmethod
    def test_get_val_integer_rational_problem():
        val = [1, -3, 2]
        problem = create_problem("Integer", "Rational", [0, 20], val)
        assert_that([1, -3, 2], equal_to(problem.get_val()))

    @staticmethod
    def test_get_solution_random_val_integer_complex_problem():
        problem = create_problem("Integer", "Complex", [0, 20])
        val = problem.get_val()
        ans = numpy.roots(val)
        assert_that([round(ans.tolist())], contains(problem.get_sol()))

    @staticmethod
    def test_get_solution_with_rational_range():
        problem = create_problem("Rational", "Rational", [1, 1, 20])
        assert_that([[]], contains(problem.get_sol()))

    @staticmethod
    def test_get_value_with_integer_solution():
        problem = create_problem("Rational", "Integer")
        assert_that(problem.get_val(), only_contains(instance_of(int)))

class UnexpectedBehaviour(TestCase):
    def test_wrongvalues_integer_rational(self):
        pass

# TODO: Test unexpected behavior


def new_arithmetic_dict():
    dict = {"problem": "Arithmetic_Polynomial_Second_degree", "desc": "blabla"}
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


def create_problem(domain="Integer", image="Rational", range=[0, 20], val=None):
    dict = new_arithmetic_dict()
    dict["domain"] = domain
    dict["image"] = image
    dict['range'] = range
    if val:
        dict["val"] = val
    problem = Problem_generator.factory(json.dumps(dict))
    return problem


def round(list):
    new_list = []
    for x in list:
        if isinstance(x, complex):
            new_list.append(complex("{0:.2f}".format(x)))
        elif isinstance(x, float):
            new_list.append(float("{0:.2f}".format(x)))
    return new_list
