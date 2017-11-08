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


def problem_settings(problem, problem_description, domain, image, range, val):
    settings = {
        "problem": problem,
        "desc": problem_description,
        "domain": domain,
        "image": image,
        "range": range
    }
    if val:
        settings["val"] = val
    return settings
