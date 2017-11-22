# encoding: utf-8
from behave import given, when, then
from django.contrib.auth.hashers import make_password
from features.pages import *


@given('I am an existing non logged professor')
def step_impl(context):
    from test.factories.user import ProfessorFactory
    u = ProfessorFactory.create(user__username="username", user__password=make_password("password"))
    u.save()


@then('I log in')
def step_impl(context):
    context.login_page.navigate(context.base_url)
    assert context.login_page.currently_on_username_page()
    context.login_page.enter_username("username")
    context.login_page.submit()
    assert context.login_page.currently_on_password_page()
    context.login_page.enter_password('password')
    context.login_page.submit()
    assert context.browser.current_url_endswith(ProfessorDashboardPageLocator.URL)


@then('I create the class "{classname}", with students "{firstname1}" "{lastname1}" and "{firstname2}" "{lastname2}"')
def step_impl(context, classname, firstname1, lastname1, firstname2, lastname2):
    context.professor_dashboard_page.click_add_class()
    assert context.create_class_page.currently_on_this_page()
    context.create_class_page.enter_class_name(classname)
    context.create_class_page.select_id_stage("13")
    context.create_class_page.submit()
    assert context.add_student_class_page.currently_on_this_page()
    context.add_student_class_page.fill_student_1_first_name(firstname1)
    context.add_student_class_page.fill_student_1_last_name(lastname1)
    context.add_student_class_page.fill_student_2_first_name(firstname2)
    context.add_student_class_page.fill_student_2_last_name(lastname2)
    context.add_student_class_page.submit()
    assert context.class_page.currently_on_this_page()


@then('I create the test "{test_name}" for skill "{skill}"')
def step_impl(context, test_name, skill):

    context.class_page.access_class_tests()
    assert context.class_page.currently_on_class_tests_page()
    context.class_page.add_new_test()
    assert context.class_page.currently_on_test_type_choice()
    context.class_page.add_online_test()
    context.add_online_test_page.currently_on_this_page()
    context.add_online_test_page.select_skill(skill)
    context.add_online_test_page.add_skill()
    context.add_online_test_page.add_skill()
    context.add_online_test_page.add_skill()
    context.add_online_test_page.add_test_name(test_name)
    context.add_online_test_page.create_test()


@given('The db is populated')
def step_impl(context):
    populate_stages_in_db()


def populate_stages_in_db():
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
