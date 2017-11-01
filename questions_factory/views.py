# encoding: utf-8

from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.db import transaction
from django.db.models import Q


def generator(request):
    if request.method == "GET":
        return render(request, "questions_factory/settings_problems.haml")
    if request.method == "POST":

        return render(request, "questions_factory/questions_list.haml")
    raise PermissionDenied()
