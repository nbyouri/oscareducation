import abc


class ProblemModel:
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_desc(self):
        """Return the description of the problem"""

    @abc.abstractmethod
    def get_sol(self):
        """Return the solution of the problem"""

    @abc.abstractmethod
    def gen_values(self):
        """Generate new random values for the problem"""

    @abc.abstractmethod
    def gen_questions(self, number_of_questions):
        """Generate questions for use in context"""

    @abc.abstractmethod
    def make_form(self):
        """Generate the associated form"""
