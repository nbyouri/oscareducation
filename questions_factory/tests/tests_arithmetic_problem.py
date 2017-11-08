from django.test import TestCase
import json
import numpy
from hamcrest import *
from questions_factory.models.problem_generator import ProblemGenerator


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
    def test_get_solution_random_val_rational_complex_problem():
        problem = create_problem("Rational", "Complex", [0, 20])
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

    def test_wrong_domain_value_raise_error(self):
        with self.assertRaises(ValueError):
            problem = create_problem("Wrong_val", "Rational")
            problem.get_sol()

    def test_wrong_image_value_raise_error(self):
        with self.assertRaises(ValueError):
            problem = create_problem("Integer", "Wrong val")
            problem.get_sol()


def new_arithmetic_dict():
    dict = {"problem": "Arithmetic_Polynomial_Second_degree", "desc": "blabla"}
    return dict


def create_problem(domain="Integer", image="Rational", range=[0, 20], val=None):
    dict = new_arithmetic_dict()
    dict["domain"] = domain
    dict["image"] = image
    dict['range'] = range
    if val:
        dict["val"] = val
    problem = ProblemGenerator.factory(json.dumps(dict))
    return problem


def round(list):
    new_list = []
    for x in list:
        if isinstance(x, complex):
            new_list.append(complex("{0:.2f}".format(x)))
        elif isinstance(x, float):
            new_list.append(float("{0:.2f}".format(x)))
    return new_list
