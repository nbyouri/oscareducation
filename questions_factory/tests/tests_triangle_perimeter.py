from django.test import TestCase
from questions_factory.models import *
import json
import numpy
import os
from hamcrest import *


class NormalBehaviour(TestCase):
    def test_basic(self):
        for i in range(0, 10000):
            tri = TrianglePerimeterProblem()
            assert_that((tri.side_a + tri.side_b > tri.side_c)
                        and (tri.side_a + tri.side_c > tri.side_b)
                        and (tri.side_b + tri.side_c > tri.side_a))


class UnexpectedBehaviour(TestCase):
    pass
