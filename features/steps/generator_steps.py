import re

from behave import given, when, then
from selenium.webdriver.support.select import Select


@then('I click on generate the question')
def step_impl(context):
    context.test_modify_page.click_on_generate_questions()


@given('I am on the generator page')
def step_impl(context):
    assert context.generator_page.currently_on_this_page()


@then("I select the simple interest problem generator")
def step_impl(context):
    context.generator_page.select_simple_interest_problem_generator()


@then("I select the arithmetic problem generator")
def step_impl(context):
    context.generator_page.select_arithmetic_problem_generator()


@then('I enter "{low}" as lower range and "{up}" as upper range')
def step_impl(context, low, up):
    context.generator_page.fill_range_from(low)
    context.generator_page.fill_range_to(up)


@when('I click on the create button')
def step_impl(context):
    context.generator_page.generate_questions()


@then('I see a list of generated problems')
def step_impl(context):
    assert context.generated_questions_page.currently_on_this_page()


@then('I see an error panel')
def step_impl(context):
    assert context.generator_page.error_displayed()


@then('I choose a generated problem')
def step_impl(context):
    context.generated_questions_page.select_generated_problem()


@then('I click on going back to the test')
def step_impl(context):
    context.generated_questions_page.go_back_to_test()


@then('I select the rational domain')
def step_impl(context):
    context.generator_page.select_rational_domain()


@then('I set the time placed to month')
def step_impl(context):
    context.generator_page.set_time_placed_to_month()


@then('I set the type of rate to month')
def step_impl(context):
    context.generator_page.set_type_rate_to_month()


