from selenium.webdriver.common.by import By
from feature_testing import Browser


class GeneratedQuestionsPageLocator(object):
    # Login page elements locator
    PAGE_TITLE = (By.ID, "id_generated_questions_page")
    SELECT_GENERATED_PROBLEM_BUTTON = (By.XPATH, "//button[@type='submit']")
    BACK_TO_TEST_BUTTON = (By.ID, "return-to-test-modify")


class GeneratedQuestionsPage(Browser):
    def navigate(self, base_url):
        pass

    # Login page actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def currently_on_this_page(self):
        return self.driver.find_element(*GeneratedQuestionsPageLocator.PAGE_TITLE)

    def select_generated_problem(self):
        self.click_element(*GeneratedQuestionsPageLocator.SELECT_GENERATED_PROBLEM_BUTTON)

    def go_back_to_test(self):
        self.click_element(*GeneratedQuestionsPageLocator.BACK_TO_TEST_BUTTON)
