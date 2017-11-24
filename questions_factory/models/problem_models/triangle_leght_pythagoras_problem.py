# 2 : As a teacher I want a functionality to create a random problem where the student will have to find the length
# of the side of a triangle (using Pythagoras theorem) In order to not having to create multiple questions manually"
from questions_factory.models import *
import math


# this code take the correct side at triangle perimeter problem, is it true?
from questions_factory.models.triangle_perimeter_problem import TrianglePerimeterProblem


class TriangleLeghtPythagorasProblem(TrianglePerimeterProblem):
    def gen_values(self):
        pass

    def get_desc(self):
        pass

    def get_sol(self):
        pass

    def make_form(self):
        pass

    def __init__(self):
        TrianglePerimeterProblem.__init__(self)
        sides = self.init_sides()
        self.side_a = sides[0]
        self.side_b = sides[1]
        self.side_c = sides[2]

    def find_side(self):
        if round(math.pow(self.side_a, 2)) + round(math.pow(self.side_b, 2)) == round(math.pow(self.side_c, 2)):
            return 0  # correct

        if round(math.pow(self.side_b, 2)) + round(math.pow(self.side_c, 2)) == round(math.pow(self.side_a, 2)):
            return 0  # correct

        if round(math.pow(self.side_a, 2)) + round(math.pow(self.side_c, 2)) == round(math.pow(self.side_b, 2)):
            return 0  # correct

        return 1  # NOT correct

# My idea: the class "find_side" must have 3 variables: a,b,c. If whit these 3 variables the method return 1, they aren't correct
# sides for a triangle rectangle
