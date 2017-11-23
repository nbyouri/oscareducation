from decimal import Decimal
from django.test import TestCase
from questions_factory.models import *
import json
import math
import os
from hamcrest import *

from questions_factory.models.triangle_leght_pythagoras_problem import TriangleLeghtPythagorasProblem

"""
class NormalBehaviour(TestCase):
    def test_basic(self):

        tri = TriangleLeghtPythagorasProblem()
        if round(math.pow(tri.side_a, 2)) + round(math.pow(tri.side_b, 2)) == round(math.pow(tri.side_c, 2)):
            s1 = 0
        else:
            s1 = 1
        if round(math.pow(tri.side_b, 2)) + round(math.pow(tri.side_c, 2)) == round(math.pow(tri.side_a, 2)):
            s2 = 0
        else:
            s2 = 1
        if round(math.pow(tri.side_a, 2)) + round(math.pow(tri.side_c, 2)) == round(math.pow(tri.side_b, 2)):
            s3 = 0
        else:
            s3 = 1

        assert_that(tri.find_side() == s1 or tri.find_side() == s2 or tri.find_side() == s3)  # HOW TO COMPLETE IT?

"""
class UnexpectedBehaviour(TestCase):
    pass
