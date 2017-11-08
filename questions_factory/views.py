# encoding: utf-8
from django.db import transaction
from django.shortcuts import render, get_object_or_404, reverse
from models import *
from examinations.models import *
from examinations.models import Test, Answer, TestExercice, TestStudent, Context, List_question
from promotions.utils import user_is_professor
from django.http import JsonResponse


@user_is_professor
def generator(request, test_exercice_pk):
    form = ArithmeticPolynomialSecondDegree.make_form(request.POST or None)
    test_exercice = get_object_or_404(TestExercice, pk=test_exercice_pk)
    if request.method == "POST":
        if form.is_valid():
            dom = form.cleaned_data['domain']
            image = form.cleaned_data['image']
            range = [int(form.cleaned_data['range_from']), int(form.cleaned_data['range_to'])]
            problem_type = "Arithmetic_Polynomial_Second_degree"
            data = {'problem': problem_type, 'image': image, 'domain': dom,
                    'range': range}
            problem = ProblemGenerator.factory(json.dumps(data))
            exercice = problem.get_context()
            with transaction.atomic():
                exercice.added_by = request.user
                test_exercice.exercice = exercice
                test_exercice.save()
            return render(request, "questions_factory/questions_list.haml",
                          {'questions': problem.gen_questions(5), 'test_exercice': test_exercice})
    return render(request, "questions_factory/settings_problems.haml", {'form': form})


def generator_submit(request, test_exercice_pk):
    test_exercice = get_object_or_404(TestExercice, pk=test_exercice_pk)
    if request.method == "POST":
        question_desc = request.POST["question_description"]
        question_source = request.POST["question_source"]
        question_answer = (request.POST["question_answer"])
        with transaction.atomic():
            question = Question(description=question_desc, answer=question_answer, source=question_source)
            question.save()
        with transaction.atomic():
            link = List_question.objects.create(
                context_id=test_exercice.exercice.id,
                question_id=question.id,
            )
            link.save()
        return JsonResponse({'msg': 'La question a été ajoutée au test'})
