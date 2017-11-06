# encoding: utf-8

import json

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from models.problem_generator import Problem_generator
from models import *
from models.problem_form import ArithmeticForm
from promotions.utils import user_is_professor


@user_is_professor
def generator(request):
    form = Arithmetic_polynomial_second_degree.make_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dom = form.cleaned_data['domain']
            image = form.cleaned_data['image']
            range = [int(form.cleaned_data['range_from']), int(form.cleaned_data['range_to'])]
            problem_type = "Arithmetic_Polynomial_Second_degree"
            data = {'problem': problem_type, 'image': image, 'domain': dom,
                    'range': range}
            problem = Problem_generator.factory(json.dumps(data))
            return render(request, "questions_factory/questions_list.haml", {'questions': problem.gen_questions(5)})
    return render(request, "questions_factory/settings_problems.haml", {'form': form})
