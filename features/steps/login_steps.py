import time
from behave import given, when, then


@given('I am on the login page')
def step_impl(context):
    time.sleep(0.2)
    context.login_page.navigate(context.base_url)
    assert context.login_page.currently_on_username_page()


@then('I enter my username')
def step_impl(context):
    time.sleep(0.2)
    context.login_page.enter_username("username")


@when('I submit my username')
def step_impl(context):
    time.sleep(0.2)
    context.login_page.submit()


@then('I am on the password page')
def step_impl(context):
    time.sleep(0.2)
    assert context.login_page.currently_on_password_page()


@then('I enter my password')
def step_impl(context):
    time.sleep(0.2)
    context.login_page.enter_password('password')


@when('I submit my password')
def step_impl(context):
    time.sleep(0.2)
    context.login_page.submit()


@given('I am an existing non logged student')
def step_impl(context):
    from test.factories.user import StudentFactory
    u = StudentFactory.create()
    u.save()


@then('I am redirected to the professor home page')
def step_impl(context):
    time.sleep(0.2)
    assert context.professor_dashboard_page.currently_on_this_page()


@then('I am redirected to the student home page')
def step_impl(context):
    time.sleep(0.2)
    assert context.student_dashboard_page.currently_on_this_page()


@then('I enter an invalid username')
def step_impl(context):
    time.sleep(0.2)
    context.login_page.enter_username('WRONGUSERNAME')


@then('I enter an invalid password')
def step_impl(context):
    time.sleep(0.2)
    context.login_page.enter_password('WRONGPASSWORD')


# NOTE : This distinction should not even occur as it gives to much information about whether a username is valid
@then('I am redirected to the login fail page')
def step_impl(context):
    time.sleep(0.2)
    assert context.login_page.currently_on_username_page() or \
           context.login_page.currently_on_password_page()
    assert context.login_page.find_alert()
