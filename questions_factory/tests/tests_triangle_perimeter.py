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


class SolutionsTests(TestCase):
    def test_time_placed_year_rate_year(self):
        problem = create_problem("cm")
        self.assertTrue(problem.get_sol() == problem.side_a + problem.side_b + problem.side_c)


class GeneratingQuestionsTests(TestCase):

    def setUp(self):
        from test.factories.skill import SkillFactory
        from test.factories.skill import SectionFactory
        SectionFactory.create(id=28, name="UAA5: Perimetre Triangle").save()
        SkillFactory.create(id=342, code="T5-U5-A1b",
                            name="", description="",
                            image="area-chart", oscar_synthese=None, modified_by_id=None, section_id=28)

    def test_mm(self):
        problem = create_problem("mm")
        questions = problem.gen_questions(5)
        self.assertTrue(isinstance(problem.get_context(), Context))
        for question in questions:
            self.assertTrue(isinstance(question, Question))
            self.assertTrue(question.description is not None)

    def test_cm(self):
        problem = create_problem("cm")
        questions = problem.gen_questions(5)
        self.assertTrue(isinstance(problem.get_context(), Context))
        for question in questions:
            self.assertTrue(isinstance(question, Question))
            self.assertTrue(question.description is not None)

    def test_dm(self):
        problem = create_problem("dm")
        questions = problem.gen_questions(5)
        self.assertTrue(isinstance(problem.get_context(), Context))
        for question in questions:
            self.assertTrue(isinstance(question, Question))
            self.assertTrue(question.description is not None)

    def test_m(self):
        problem = create_problem("m")
        questions = problem.gen_questions(5)
        self.assertTrue(isinstance(problem.get_context(), Context))
        for question in questions:
            self.assertTrue(isinstance(question, Question))
            self.assertTrue(question.description is not None)


class InstanceTests(TestCase):
    def test_of_instantiation_via_generator(self):
        problem = create_problem()
        self.assertTrue(isinstance(problem, TrianglePerimeterProblem))

    def test_of_raw_instantiation(self):
        problem = TrianglePerimeterProblem("cm")
        self.assertTrue(isinstance(problem, TrianglePerimeterProblem))

    def test_of_instantiation_with_wrong_values(self):
        with self.assertRaises(ValueError):
            TrianglePerimeterProblem("wrong")


# Utils

def create_problem(unit="cm"):
    values = new_triangle_perimeter_values()
    values[unit] = unit
    problem = ProblemGenerator.factory(json.dumps(values))
    return problem


def new_triangle_perimeter_values():
    return {"problem": "Triangle_Perimeter_Problem"}
