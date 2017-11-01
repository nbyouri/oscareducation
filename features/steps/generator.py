from behave import given, when, then
from django.contrib.auth.hashers import make_password


@given('I am on the generator page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/questions_factory/generator/')
    assert br.current_url.endswith('/questions_factory/generator/')
