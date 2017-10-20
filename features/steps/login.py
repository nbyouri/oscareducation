from behave import given, when, then


@given('an existing non logged professor')
def step_impl(context):
    from test.factories.user import ProfessorFactory
    u = ProfessorFactory.create()
    u.save()


@given('an existing non logged student')
def step_impl(context):
    from test.factories.user import StudentFactory
    u = StudentFactory.create()
    u.save()


@when('I submit a valid login page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/accounts/usernamelogin/')
    br.find_element_by_id("id_username").send_keys('username')
    br.find_element_by_xpath("//input[@type='submit']").click()
    assert br.current_url.endswith('/accounts/passwordlogin/')
    br.find_element_by_id("id_password").send_keys('password')
    br.find_element_by_xpath("//input[@type='submit']").click()


@then('I am redirected to the professor home page')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/professor/dashboard/')


@then('I am redirected to the student home page')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/student/dashboard/')


@when('I submit an invalid username')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/accounts/usernamelogin/')
    br.find_element_by_id("id_username").send_keys('WRONGUSERNAME')
    br.find_element_by_xpath("//input[@type='submit']").click()


@when('I submit an invalid password but valid account')
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
    assert br.current_url.endswith('/accounts/passwordlogin/') or br.current_url.endswith('/accounts/usernamelogin/')
    assert br.find_element_by_class_name('alert-danger')
