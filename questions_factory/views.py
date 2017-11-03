# encoding: utf-8

import json

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from models.problem_generator import Problem_generator
from models.problem_form import ArithmeticForm


def generator(request):
    if request.method == "GET":
        form = ArithmeticForm()
        return render(request, "questions_factory/settings_problems.haml", {'form': form})
    if request.method == "POST":
        # TODO Verify data send in POST
        dom = request.POST['domain']
        image = request.POST['image']
        range = [int(request.POST['range_from']), int(request.POST['range_to'])]
        problem_type = "Arithmetic_Polynomial_Second_degree"
        data = {'problem': problem_type, 'image': image, 'domain': dom,
                'range': range}
        problem = Problem_generator.factory(json.dumps(data))
        return render(request, "questions_factory/questions_list.haml", {'questions': problem.gen_questions(5)})
    raise PermissionDenied()
