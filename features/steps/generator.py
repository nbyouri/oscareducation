from behave import given, when, then
from django.contrib.auth.hashers import make_password


@given('I am on the generator page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/questions_factory/generator/')
    assert br.current_url.endswith('/questions_factory/generator/')


@then('I enter "{low}" as lower range and "{up}" as upper range')
def step_impl(context, low, up):
    br = context.browser
    br.find_element_by_id("id_range_from").send_keys(low)
    br.find_element_by_id("id_range_to").send_keys(up)


@when('I click on the create button')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("id_generate_button").click()


@then('I see a list of generated problems')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id("id_generated_questions_page")


@then('I see an error panel')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id("id_error_panel")

