import re

from behave import given, when, then
from selenium.webdriver.support.select import Select


@given('I am on the generator page')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id("id_question_generator")


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


@then('I access the class test page')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("id_my_tests_button").click()
    assert re.search(r'/professor/lesson/[0-9]+/test/', br.current_url)


@then('I click on add a test')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("id_add_test_button").click()
    assert re.search(r'/professor/lesson/[0-9]+/test/add', br.current_url)


@then('I click on add a test online')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("id_add_test_online_button").click()
    assert re.search(r'/professor/lesson/[0-9]+/test/online/add', br.current_url)


@then('I select the skill "{skill_code}"')
def step_impl(context, skill_code):
    br = context.browser
    Select(br.find_element_by_xpath("//select[@ng-model='stage13SelectedSkill']")).select_by_value(skill_code)


@then('I add that competence')
def step_impl(context):
    br = context.browser
    # TODO : This is actually really stupid, must adapt to a laggy response from Angular when clicking !
    br.find_element_by_id("addSkillToTestButtonForStage13").click()
    br.find_element_by_id("addSkillToTestButtonForStage13").click()
    br.find_element_by_id("addSkillToTestButtonForStage13").click()


@then('I add a name to that test')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("test_name").send_keys("foo_test")


@then('I create the test')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("id_create_test_button").click()
    # assert re.search(r'/professor/lesson/[0-9]+/test/online/[0-9]+/modify/', br.current_url)


@then('I click on generate the question')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("id_generate_button").click()

