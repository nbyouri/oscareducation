from datetime import datetime
from selenium import webdriver
import django
from django.test.runner import DiscoverRunner
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.shortcuts import resolve_url
import os
import codecs
from features import Browser
from features.pages import *
os.environ['DJANGO_SETTINGS_MODULE'] = 'oscar.settings'


def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.old_db_config = context.test_runner.setup_databases()
    context.browser = Browser()

    # Page Objects
    context.login_page = LoginPage()
    context.professor_dashboard_page = ProfessorDashboardPage()
    context.student_dashboard_page = StudentDashboardPage()
    context.create_class_page = CreateClassPage()
    context.add_student_class_page = AddStudentClassPage()
    context.class_page = ClassPage()
    context.add_online_test_page = AddOnlineTestPage()
    context.test_modify_page = TestModifyPage()
    context.generator_page = GeneratorPage()
    context.generated_questions_page = GeneratedQuestionsPage()


class BehaviorDrivenTestCase(StaticLiveServerTestCase):
    """
    Test case attached to the context during behave execution
    This test case prevents the regular tests from running.
    """

    def runTest(*args, **kwargs):
        pass


def before_scenario(context, _):
    context.test = BehaviorDrivenTestCase()
    context.test.setUpClass()
    context.test() # this starts a transaction

    context.base_url = context.test.live_server_url

    def get_url(to=None, *args, **kwargs):
        return context.base_url + (
            resolve_url(to, *args, **kwargs) if to else '')
    context.get_url = get_url


def after_scenario(context, _):
    pass


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.browser.quit()
    context.test_runner.teardown_databases(context.old_db_config)


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass


# After a single step
def after_step(context, step):
    if step.status == 'failed':
        context.browser.save_screen_shot(context, step)
