# coding=utf-8
import random
from collections import OrderedDict

from fractions import Fraction
import numpy
import math

from examinations.models import *
from questions_factory.models.problem_form import ArithmeticForm
from questions_factory.models.problem_models.problem import *
from skills.models import Skill


class ArithmeticPolynomialSecondDegree(Problem):
    def __init__(self, domain, image, range=(0, 20), val=None):
        Problem.__init__(self)
        self.desc = "Polynomial second degree"
        self.domain = domain
        self.image = image
        self.range = range
        if val and len(val) == 3:
            self.val = val
        else:
            self.gen_new_values()

    def gen_new_values(self):
        self.val = list()
        self.gen_values()

    def gen_values(self):
        if self.image == "Integer":
            self.gen_values_from_sol()
        elif self.domain == "Integer":
            for i in range(3):
                self.val.append(random.randint(self.range[0], self.range[1]))
        elif self.domain == "Rational":
            for i in range(3):
                self.val.append(random.uniform(self.range[0], self.range[1]))
        else:
            raise ValueError("Wrong value for domain: ", self.domain)
        if self.val[0] == 0:
            self.val[0] = 1

    def gen_values_from_sol(self):
        # Max_val for value is rng_range³
        # TODO What range should we put ?
        sol = [random.randint(-5, 5), random.randint(-5, 5)]
        sum, prod = sol[0] + sol[1], sol[0] * sol[1]
        # For polynom of type ax²+bx+c
        a = random.randint(-5, 5)
        b = -1 * sum * a
        c = prod * a
        self.val = [a, b, c]

    def get_desc(self):
        return self.desc

    def get_val(self):
        return self.val

    @staticmethod
    def round(list):
        new_list = []
        for x in list:
            if isinstance(x, complex):
                new_list.append(complex("{0:.2f}".format(x)))
            elif isinstance(x, float):
                new_list.append(float("{0:.2f}".format(x)))
        return new_list

    def get_sol(self):
        tmp_sol = numpy.roots(self.val).tolist()
        sol = list()
        if self.image == "Rational" or self.image == "Integer":
            # sol = list()
            # for root in tmp_sol:
            if not isinstance(tmp_sol[0], complex):
                # sol.append(root)
                sol = (self.compute_sol())
        elif self.image == "Complex":
            for root in tmp_sol:
                sol.append(str(root))
        else:
            raise ValueError("Wrong value for image:", self.image)

        #  return self.round(sol)
        return sol

    def rho(self):
        return self.val[1] ** 2 - 4 * self.val[0] * self.val[2]

    def compute_sol(self):
        #return [r"\frac{2-\sqrt{2}}{3}"+','+r"\frac{3}{2}"]
        rho = self.rho()
        sqrt_rho = math.sqrt(rho)
        num_neg = -1 * self.val[1] - math.sqrt(rho)
        num_pos = -1 * self.val[1] + math.sqrt(rho)
        if self.domain == "Integer" or self.image == "Integer":
            num_neg = int(num_neg)
            num_pos = int(num_pos)
        den = 2 * self.val[0]
        ans1, ans2 = "0", "0"

        if sqrt_rho.is_integer():
            if num_neg % den == 0:
                ans1 = self.simple_answer(num_neg, den)
                # ans1 = ans1.format(num_neg / den)
                # ans1 = latex(sympify(str(num_neg/den)))
            else:
                ans1 = self.ans_with_frac(num_neg, den, True)
                # ans1 = ans1.format(num_neg, den)
                # ans1 = latex(sympify(str(num_neg)+"/"+str(den), evaluate=False))
            if num_pos % den == 0:
                ans2 = self.simple_answer(num_pos, den)
                #ans2 = ans2.format(num_pos / den)
                # ans2 = latex(sympify(str(num_pos/den)))
            else:
                ans2 = self.ans_with_frac(num_pos, den, True)
                #ans2 = ans2.format(num_pos, den)
                # ans2 = latex(sympify(str(num_pos) + "/" + str(den), evaluate=False))
        else:
            pass
            ans1 = self.ans_with_root(rho, "-") #.format(-1 * self.val[1], rho, 2 * self.val[2])
            ans2 = self.ans_with_root(rho, "+") #.format(-1 * self.val[1], rho, 2 * self.val[2])
            # ans1 = latex(sympify("("+"-"+str(self.val[1])+"-"+str(math.sqrt(rho))+")"+"/"+str(den), evaluate=False))
            # ans2 = latex(sympify("("+"-" + str(self.val[1]) + "+" + str(math.sqrt(rho))+ ")"+ "/" + str(den), evaluate=False))
        return [ans1 + ',' + ans2, ans2 + ',' + ans1]

    def new_question(self, sol):
        question_desc = "Calculer les racines de: "
        if self.domain == "Integer":
            equation = ("{:-d}x²{:+d}x{:+d}".format(self.val[0], self.val[1], self.val[2]))
        elif self.domain == "Rational":
            equation = ("{:-0.2f}x²{:+0.2f}x{:+0.2f}".format(self.val[0], self.val[1], self.val[2]))
        equation = self.pretty_polynomial_string(equation)
        question_desc += equation
        # if sol.__len__() > 1:
        #     sol = tuple(sol)
        # else:
        #     sol = sol[0]
        answers = yaml.dump(OrderedDict([("answers", sol), ("type", "math-advanced")]))
        question = Question(description=question_desc, answer=answers, source="Génerée automatiquement")
        return question

    def gen_questions(self, number_of_questions):
        questions = list()
        for _ in range(number_of_questions):
            # We only want problems having a solution
            # TODO : Avoid looping
            while not self.get_sol():
                self.gen_new_values()
            questions.append((self.new_question(self.get_sol())))
            # TODO : Check if no two problems the same
            self.gen_new_values()
        return questions

    def get_context(self):
        default_context = self.default_context()
        # TODO Get from db if already Context already exist
        # context, created = Context.objects.get_or_create(defaults=default_context, file_name="generated")
        return default_context

    @staticmethod
    def default_context():
        description = "Calculer les racines $$ x_1, x_2 $$ d'un polyonme du second degré <br/> " \
                      "<b> Attention : </b> les réponses doivent être sous la forme " \
                      "$$ x_1, x_2 $$ les réponses sous formes de fractions doivent être simplifiés au maximum <br/>" \
                      "utilisez le clavier spécial pour taper vos réponses sous formes d'équations"
        skill_id = "T4-U5-A1b"
        default_context = Context.objects.create(
            file_name="generated",
            skill=Skill.objects.get(code=skill_id),
            context=description,
            added_by=None
        )
        return default_context

    @staticmethod
    def make_form(post_values):
        return ArithmeticForm(post_values)

    def ans_with_root(self, rho, sign):
        #if self.domain == "Integer" or self.image == "Integer":
        return r"\frac{" + str(-1*self.val[1]) + sign + "\sqrt{" + str(rho) + "}}{" + str(2*self.val[2]) +"}"
        # else:
        #     return r"\frac{{:+f}}+\sqrt{{:-f}}}}{{:-f}}"

    def ans_with_frac(self, num, den, simplify=False):
        if not simplify:
            return r"\frac{" + str(num) + "}{" + str(den) + "}"
        else:
            f = Fraction(num, den)
            return r"\frac{" + str(f.numerator) + "}{" + str(f.denominator) + "}"

    def simple_answer(self, num, den):
        # if self.domain == "Integer" or self.image == "Integer":
        return str(num/den)
        # else:
        #     return "{:-f}"

    @staticmethod
    # TODO Make it prettier
    def pretty_polynomial_string(string):
        string = re.sub(r"\+-", r"-", string)
        string = "   " + string + "   "
        string = re.sub(r"(\+|-|\s)0x*²*(\+|-|\s)", r"\2", string)
        string = re.sub(r"(\+|-|\s)1(x²*)(\+|-|\s)", r"\2\3", string)
        return string
