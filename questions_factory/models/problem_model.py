import abc


class Problem_model:
    def __init__(self, desc, domain, range, val=None):
        self.desc = desc
        self.domain = domain
        self.range = range

    @abc.abstractmethod
    def get_desc(self):
        """Return the description of the problem"""
        return

    @abc.abstractmethod
    def get_sol(self):
        """Return the solution of the problem"""
        return

    @abc.abstractmethod
    def gen_values(self):
        """Generate new random values for the problem"""
