# encoding: utf-8

from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.db import transaction
from django.db.models import Q

def generator(request):
    # GET
    if request.method == "GET":
        return render(request, "questions_factory/generator.haml")
    raise PermissionDenied()
