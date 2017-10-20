from behave import given, when, then


@given('an anonymous professor')
def step_impl(context):
    from test.factories.user import ProfessorFactory
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = ProfessorFactory.create()
    # Don't omit to call save() to insert object in database
    u.save()


@given('an anonymous student')
def step_impl(context):
    from test.factories.user import StudentFactory
    u = StudentFactory.create()
    u.save()


@when('I submit a valid login page')
def step_impl(context):
    # br is an instance of Browser()
    br = context.browser
    br.get(context.base_url + '/accounts/usernamelogin/')
    # Fill login form and submit it (valid version)
    br.find_element_by_id("id_username").send_keys('username')
    br.find_element_by_xpath("//input[@type='submit']").click()
    assert br.current_url.endswith('/accounts/passwordlogin/')
    br.find_element_by_id("id_password").send_keys('password')
    br.find_element_by_xpath("//input[@type='submit']").click()


@then('I am redirected to the professor home page')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/professor/dashboard/')
    # Not sure how to assert the following thing, solely previous one seems good enough
    # assert br.find_element_by_id('main_title').text == "Login success"


@then('I am redirected to the student home page')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/student/dashboard/')


@when('I submit an invalid login page')
def step_impl(context):
    br = context.browser

    br.get(context.base_url + '/accounts/usernamelogin/')
    br.find_element_by_id("id_username").send_keys('username')
    br.find_element_by_xpath("//input[@type='submit']").click()
    assert br.current_url.endswith('/accounts/passwordlogin/')
    br.find_element_by_id("id_password").send_keys('wrongpassword')
    br.find_element_by_xpath("//input[@type='submit']").click()


@then('I am redirected to the login fail page')
def step_impl(context):
    br = context.browser
    # Checks redirection URL
    assert br.current_url.endswith('/accounts/passwordlogin/')
    assert br.find_element_by_class_name('alert-danger')
