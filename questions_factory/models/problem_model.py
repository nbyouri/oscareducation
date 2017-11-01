import abc


class Problem_model:
    def __init__(self, desc, domain, range, val=None):
        self.desc = desc
        self.domain = domain
        self.range = range

    @abc.abstractmethod
    def getDesc(self):
        """Return the description of the problem"""
        return

    @abc.abstractmethod
    def getSol(self):
        """Return the solution of the problem"""
        return

    @abc.abstractmethod
    def genValues(self):
        """Generate new random values for the problem"""
