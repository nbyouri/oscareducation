import time
from behave import given, when, then


@then('I click on generate the question')
def step_impl(context):
    time.sleep(1)
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


@then("I select the statistic problem generator")
def step_impl(context):
    context.generator_page.select_statistic_problem_generator()


@then('I enter "{low}" as lower range and "{up}" as upper range')
def step_impl(context, low, up):
    context.generator_page.fill_range_from(low)
    context.generator_page.fill_range_to(up)


@then('I enter "{elements}" elements asked')
def step_impl(context, elements):
    context.generator_page.fill_statistic_elements(elements)


@when('I click on the create button')
def step_impl(context):
    time.sleep(2)
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


@then('I set the time placed to "{time}"')
def step_impl(context, time):
    context.generator_page.set_time_placed_to(time)


@then('I set the type of rate to "{time}"')
def step_impl(context, time):
    context.generator_page.set_type_rate_to(time)


