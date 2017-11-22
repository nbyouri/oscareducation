from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from features import Browser


class GeneratorPageLocator(object):
    # Login page elements locator
    PAGE_TITLE = (By.ID, "id_question_generator")
    RANGE_FROM_INPUT = (By.ID, "id_range_from")
    RANGE_TO_INPUT = (By.ID, "id_range_to")
    DOMAIN_SELECT = (By.ID, "id_domain")
    GENERATE_BUTTON = (By.ID, "id_generate_button")
    ERROR = (By.ID, "id_error_panel")


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

    def fill_range_from(self, value):
        self.fill(value, *GeneratorPageLocator.RANGE_FROM_INPUT)

    def fill_range_to(self, value):
        self.fill(value, *GeneratorPageLocator.RANGE_TO_INPUT)

    def select_rational_domain(self):
        self.select("Rational", *GeneratorPageLocator.DOMAIN_SELECT)

    def generate_questions(self):
        self.click_element(*GeneratorPageLocator.GENERATE_BUTTON)

    def currently_on_this_page(self):
        return self.driver.find_element(*GeneratorPageLocator.PAGE_TITLE)

    def error_displayed(self):
        return self.driver.find_element(*GeneratorPageLocator.ERROR)
