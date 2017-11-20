from decimal import Decimal
from django.test import TestCase
from questions_factory.models import *
import json
import numpy
import os
from hamcrest import *

from questions_factory.models.triangle_area_problem import TriangleAreaProblem


class NormalBehaviour(TestCase):
    def test_basic(self):
        tri = TriangleAreaProblem()
        s = tri.side_a + tri.side_b + tri.side_c
        s = s / 2.0
        output1 = Decimal(numpy.math.sqrt(s * (s - tri.side_a) * (s - tri.side_b) * (s - tri.side_c)))  # erone method
        test_area = round(output1, 2)
        area = tri.area()
        assert_that(tri.area() == test_area)



class UnexpectedBehaviour(TestCase):
    pass
