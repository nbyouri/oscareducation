# encoding: utf-8
from behave import given, when, then
from django.contrib.auth.hashers import make_password
from features.pages import *


@given('I am an existing non logged professor')
def step_impl(context):
    from test.factories.user import ProfessorFactory
    u = ProfessorFactory.create(user__username="username", user__password=make_password("password"))
    u.save()


@then('I log in')
def step_impl(context):
    context.login_page.navigate(context.base_url)
    assert context.login_page.currently_on_username_page()
    context.login_page.enter_username("username")
    context.login_page.submit()
    assert context.login_page.currently_on_password_page()
    context.login_page.enter_password('password')
    context.login_page.submit()
    assert context.browser.current_url_endswith(ProfessorDashboardPageLocator.URL)


@then('I create the class "{classname}", with students "{firstname1}" "{lastname1}" and "{firstname2}" "{lastname2}"')
def step_impl(context, classname, firstname1, lastname1, firstname2, lastname2):
    context.professor_dashboard_page.click_add_class()
    assert context.create_class_page.currently_on_this_page()
    context.create_class_page.enter_class_name(classname)
    context.create_class_page.select_id_stage("13")
    context.create_class_page.submit()
    assert context.add_student_class_page.currently_on_this_page()
    context.add_student_class_page.fill_student_1_first_name(firstname1)
    context.add_student_class_page.fill_student_1_last_name(lastname1)
    context.add_student_class_page.fill_student_2_first_name(firstname2)
    context.add_student_class_page.fill_student_2_last_name(lastname2)
    context.add_student_class_page.submit()
    assert context.class_page.currently_on_this_page()


@then('I create the test "{test_name}" for skill "{skill}"')
def step_impl(context, test_name, skill):

    context.class_page.access_class_tests()
    assert context.class_page.currently_on_class_tests_page()
    context.class_page.add_new_test()
    assert context.class_page.currently_on_test_type_choice()
    context.class_page.add_online_test()
    context.add_online_test_page.currently_on_this_page()
    context.add_online_test_page.select_skill(skill)
    context.add_online_test_page.add_skill()
    context.add_online_test_page.add_skill()
    context.add_online_test_page.add_skill()
    context.add_online_test_page.add_test_name(test_name)
    context.add_online_test_page.create_test()
