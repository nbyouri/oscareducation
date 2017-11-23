# coding=utf-8
import django
import time
from django.test.runner import DiscoverRunner
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.shortcuts import resolve_url
import os
from pages import *
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
    context.test()  # this starts a transaction
    context.base_url = context.test.live_server_url
    # Fill test database with test data
    populate_db()

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


def before_step(context, step):
    time.sleep(0.01)


# After a single step
def after_step(context, step):
    if step.status == 'failed':
        context.browser.save_screen_shot(context, step)


def populate_db():
    from test.factories.stage import StageFactory
    from test.factories.skill import SkillFactory
    from test.factories.skill import SectionFactory

    SectionFactory.create(id=28, name="UAA5: Deuxième degré").save()

    skilla = SkillFactory.create(id=342, code="T4-U5-A1b",
                        name="Résoudre algébriquement une équation ou une inéquation du 2e degré", description="",
                        image="area-chart", oscar_synthese=None, modified_by_id=None, section_id=28)

    skilla.save()

    StageFactory.create(id=1, name="étape I (1er degré primaire)", short_name="1e", level=1,
                        previous_stage_id=None).save()
    StageFactory.create(id=9, name="étape II (2e et 3e degrés primaire)", short_name="2e", level=2,
                        previous_stage_id=1).save()
    StageFactory.create(id=3, name="étape III (1er degré secondaire)", short_name="3e", level=3,
                        previous_stage_id=9).save()
    StageFactory.create(id=10, name="2e degré professionnel", short_name="2p", level=4,
                        previous_stage_id=3).save()
    StageFactory.create(id=11, name="3e degré professionnel", short_name="3p", level=5,
                        previous_stage_id=10).save()
    StageFactory.create(id=18, name="2e degré technique (2 pér./sem.)", short_name="2d2", level=4,
                        previous_stage_id=3).save()
    StageFactory.create(id=19, name="3e degré technique (2 pér./sem.)", short_name="3d2", level=5,
                        previous_stage_id=18).save()
    StageFactory.create(id=12, name="3e année transition", short_name="3t", level=4,
                        previous_stage_id=3).save()
    StageFactory.create(id=13, name="4e année transition", short_name="4t", level=5,
                        previous_stage_id=12, skills=(skilla,)).save()
    StageFactory.create(id=14, name="5e année transition (mathématiques de base)", short_name="5tb", level=6,
                        previous_stage_id=13).save()
    StageFactory.create(id=15, name="6e année transition (mathématiques de base)", short_name="6tb", level=7,
                        previous_stage_id=14).save()
    StageFactory.create(id=16, name="5e année transition (mathématiques générales)", short_name="5tg", level=6,
                        previous_stage_id=13).save()
    StageFactory.create(id=17, name="6e année transition (mathématiques générales)", short_name="6tg", level=7,
                        previous_stage_id=16).save()