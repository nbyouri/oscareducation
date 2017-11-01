# encoding: utf-8

from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from models.problem_generator import Problem_generator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.db import transaction
from django.db.models import Q


def generator(request):
    if request.method == "GET":
        return render(request, "questions_factory/settings_problems.haml")
    if request.method == "POST":
        dom = request.POST.domain
        range = request.POST.range_to,  request.POST.range_from
        problem_type = "Arithmetic_Polynomial_Second_degree"
        problem = Problem_generator.factory(problem_type, dom, range)
        return render(request, "questions_factory/questions_list.haml", {'questions' : None})
    raise PermissionDenied()
