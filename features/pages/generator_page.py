from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from features import Browser


class GeneratorPageLocator(object):
    # Login page elements locator
    NB_QUESTIONS_INPUT = (By.ID, "id_nb_question")

    PAGE_TITLE = (By.ID, "id_question_generator")
    GENERATOR_TYPE_SELECTOR = (By.ID, "id_generator_name")
    RANGE_FROM_INPUT = (By.ID, "id_range_from")
    RANGE_TO_INPUT = (By.ID, "id_range_to")
    DOMAIN_SELECT = (By.ID, "id_domain")
    GENERATE_BUTTON = (By.ID, "id_generate_button")
    ERROR = (By.ID, "id_error_panel")

    ARITHMETIC_PROBLEM_GENERATOR = "ArithmeticProblem"
    SIMPLE_INTEREST_PROBLEM_GENERATOR = "SimpleInterestProblem"
    STATISTIC_PROBLEM_GENERATOR = "StatisticsProblem"
    VOLUME_PROBLEM_GENERATOR = "VolumeProblem"

    # Interest form
    TIME_PLACED_SELECTOR = (By.ID, "id_time_placed")
    TYPE_RATE_SELECTOR = (By.ID, "id_type_rate")

    # Statistic form
    NB_ELEMENTS = (By.ID, "id_nb")

    # Volume form
    OBJECT_VOLUME_SELECTOR = (By.ID, "id_object_type")
    CYLINDER_SELECT_OPTION = 'cylinder'
    PYRAMID_SELECT_OPTION = 'pyramid'
    PRISM_SELECT_OPTION = 'prism'
    CUBE_SELECT_OPTION = 'cube'
    CONE_SELECT_OPTION = 'cone'


class GeneratorPage(Browser):
    def navigate(self, base_url):
        pass

    # Login page actions

    def generate_questions(self):
        self.click_element(*GeneratorPageLocator.GENERATE_BUTTON)

    def currently_on_this_page(self):
        return self.driver.find_element(*GeneratorPageLocator.PAGE_TITLE)

    def error_displayed(self):
        return self.driver.find_element(*GeneratorPageLocator.ERROR)

    def select_number_of_questions(self, number):
        self.fill(number, *GeneratorPageLocator.NB_QUESTIONS_INPUT)

    # Arithmetic Setup

    def select_arithmetic_problem_generator(self):
        self.select(GeneratorPageLocator.ARITHMETIC_PROBLEM_GENERATOR,
                    *GeneratorPageLocator.GENERATOR_TYPE_SELECTOR)

    def fill_range_from(self, value):
        self.fill(value, *GeneratorPageLocator.RANGE_FROM_INPUT)

    def fill_range_to(self, value):
        self.fill(value, *GeneratorPageLocator.RANGE_TO_INPUT)

    def select_rational_domain(self):
        self.select("Rational", *GeneratorPageLocator.DOMAIN_SELECT)

    # Simple Interest

    def select_simple_interest_problem_generator(self):
        self.select(GeneratorPageLocator.SIMPLE_INTEREST_PROBLEM_GENERATOR,
                    *GeneratorPageLocator.GENERATOR_TYPE_SELECTOR)

    def set_time_placed_to(self, time):
        self.select(time, *GeneratorPageLocator.TIME_PLACED_SELECTOR)

    def set_type_rate_to(self, time):
        self.select(time, *GeneratorPageLocator.TYPE_RATE_SELECTOR)

    # Statistics
    def select_statistic_problem_generator(self):
        self.select(GeneratorPageLocator.STATISTIC_PROBLEM_GENERATOR, *GeneratorPageLocator.GENERATOR_TYPE_SELECTOR)

    def fill_statistic_elements(self, number):
        self.fill(number, *GeneratorPageLocator.NB_ELEMENTS)

    # Volume

    def select_volume_problem_generator(self):
        self.select(GeneratorPageLocator.VOLUME_PROBLEM_GENERATOR, *GeneratorPageLocator.GENERATOR_TYPE_SELECTOR)

    def select_volume_object_cylinder(self):
        self.select(GeneratorPageLocator.CYLINDER_SELECT_OPTION, *GeneratorPageLocator.OBJECT_VOLUME_SELECTOR)

    def select_volume_object_pyramid(self):
        self.select(GeneratorPageLocator.PYRAMID_SELECT_OPTION, *GeneratorPageLocator.OBJECT_VOLUME_SELECTOR)

    def select_volume_object_cone(self):
        self.select(GeneratorPageLocator.CONE_SELECT_OPTION, *GeneratorPageLocator.OBJECT_VOLUME_SELECTOR)

    def select_volume_object_prism(self):
        self.select(GeneratorPageLocator.PRISM_SELECT_OPTION, *GeneratorPageLocator.OBJECT_VOLUME_SELECTOR)

    def select_volume_object_cube(self):
        self.select(GeneratorPageLocator.CUBE_SELECT_OPTION, *GeneratorPageLocator.OBJECT_VOLUME_SELECTOR)

