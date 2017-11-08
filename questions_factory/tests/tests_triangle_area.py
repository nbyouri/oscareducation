from django.test import TestCase
from questions_factory.models import *
import json
import numpy
import os
from hamcrest import *

from questions_factory.models.triangle_area_problem import TriangleAreaProblem


def test_basic():
    tri = TriangleAreaProblem()
    tri.side_a = 2
    tri.side_b = 2
    tri.side_c = 2
    assert_that(tri.area == 1.73)


class NormalBehaviour(TestCase):
    pass


class NormalBehaviour(TestCase):
    pass


class UnexpectedBehaviour(TestCase):
    pass
