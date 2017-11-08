from django.test import TestCase
from questions_factory.models import *
import json
import numpy
import os
from hamcrest import *


class NormalBehaviour(TestCase):
    pass


class UnexpectedBehaviour(TestCase):
    def test_problem_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            problem_set = problem_settings("foo", "bar", "Interrzger", "Ratdqdional", [9687, 20], None)
            Problem_generator.factory(json.dumps(problem_set))
        self.assertTrue('Wrong problem type' in context.exception)


def new_arithmetic_dict():
    dict = {"problem": "Arithmetic_Polynomial_Second_degree", "desc": "blabla"}
    return dict


def problem_settings(problem, problem_description, domain, image, range, val):
    dict = {
        "problem": problem,
        "desc": problem_description,
        "domain": domain,
        "image": image,
        "range": range
    }
    if val:
        dict["val"] = val
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

