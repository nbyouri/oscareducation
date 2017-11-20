from django.test import TestCase
import json

from examinations.models import *
from questions_factory.models import SimpleInterestProblem, ProblemGenerator


class SolutionsTests(TestCase):
    def test_time_placed_year_rate_year(self):
        problem = create_problem("year", "year")
        self.assertTrue(problem.get_sol() == problem.round(problem.amount * problem.time * problem.rate))

    def test_time_placed_month_rate_month(self):
        problem = create_problem("month", "month")
        self.assertTrue(problem.get_sol() == problem.round(problem.amount * problem.time * problem.rate))

    def test_time_placed_month_rate_year(self):
        problem = create_problem("month", "year")
        self.assertTrue(problem.get_sol() == problem.round(problem.amount * (problem.time / 12) * problem.rate))

    def test_time_placed_year_rate_month(self):
        problem = create_problem("year", "month")
        self.assertTrue(problem.get_sol() == problem.round(problem.amount * problem.time * 12 * problem.rate))


class GeneratingQuestionsTests(TestCase):
    def test_time_placed_year_rate_year(self):
        problem = create_problem("year", "year")
        questions = problem.gen_questions(5)
        for question in questions:
            self.assertTrue(isinstance(question, Question))
            self.assertTrue(question.description is not None)

    def test_time_placed_month_rate_month(self):
        problem = create_problem("month", "month")
        questions = problem.gen_questions(5)
        for question in questions:
            self.assertTrue(isinstance(question, Question))
            self.assertTrue(question.description is not None)

    def test_time_placed_month_rate_year(self):
        problem = create_problem("month", "year")
        questions = problem.gen_questions(5)
        for question in questions:
            self.assertTrue(isinstance(question, Question))
            self.assertTrue(question.description is not None)

    def test_time_placed_year_rate_month(self):
        problem = create_problem("year", "month")
        questions = problem.gen_questions(5)
        for question in questions:
            self.assertTrue(isinstance(question, Question))
            self.assertTrue(question.description is not None)


class InstanceTests(TestCase):
    def test_of_instantiation_via_generator(self):
        problem = create_problem()
        self.assertTrue(isinstance(problem, SimpleInterestProblem))

    def test_of_raw_instantiation(self):
        problem = SimpleInterestProblem("year", "year")
        self.assertTrue(isinstance(problem, SimpleInterestProblem))

    def test_of_instantiation_with_wrong_values(self):
        with self.assertRaises(ValueError):
            SimpleInterestProblem("wrong", "year")
        with self.assertRaises(ValueError):
            SimpleInterestProblem("year", "wrong")
        with self.assertRaises(ValueError):
            SimpleInterestProblem("month", "wrong")
        with self.assertRaises(ValueError):
            SimpleInterestProblem("wrong", "month")
        with self.assertRaises(ValueError):
            SimpleInterestProblem("wrong", "wrong")


# Utils

def create_problem(time_placed="year", type_rate="year"):
    values = new_interest_values()
    values["time_placed"] = time_placed
    values["type_rate"] = type_rate
    problem = ProblemGenerator.factory(json.dumps(values))
    return problem


def new_interest_values():
    return {"problem": "Simple_Interest_Problem"}
