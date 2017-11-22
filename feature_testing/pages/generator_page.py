from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from feature_testing import Browser


class GeneratorPageLocator(object):
    # Login page elements locator
    PAGE_TITLE = (By.ID, "id_question_generator")
    GENERATOR_TYPE_SELECTOR = (By.ID, "id_generator_name")
    RANGE_FROM_INPUT = (By.ID, "id_range_from")
    RANGE_TO_INPUT = (By.ID, "id_range_to")
    DOMAIN_SELECT = (By.ID, "id_domain")
    GENERATE_BUTTON = (By.ID, "id_generate_button")
    ERROR = (By.ID, "id_error_panel")

    ARITHMETIC_PROBLEM_GENERATOR = "ArithmeticProblem"
    SIMPLE_INTEREST_PROBLEM_GENERATOR = "SimpleInterestProblem"
    STATISTICS_PROBLEM = "StatisticsProblem"
    VOLUME_PROBLEM = "VolumeProblem"

    TIME_PLACED_SELECTOR = (By.ID, "id_time_placed")
    TYPE_RATE_SELECTOR = (By.ID, "id_type_rate")


class GeneratorPage(Browser):
    def navigate(self, base_url):
        pass

    # Login page actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def select(self, text, *locator):
        Select(self.driver.find_element(*locator)).select_by_value(text)

    def generate_questions(self):
        self.click_element(*GeneratorPageLocator.GENERATE_BUTTON)

    def currently_on_this_page(self):
        return self.driver.find_element(*GeneratorPageLocator.PAGE_TITLE)

    def error_displayed(self):
        return self.driver.find_element(*GeneratorPageLocator.ERROR)

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

    def set_time_placed_to_month(self):
        self.select("month", *GeneratorPageLocator.TIME_PLACED_SELECTOR)

    def set_type_rate_to_month(self):
        self.select("month", *GeneratorPageLocator.TYPE_RATE_SELECTOR)
