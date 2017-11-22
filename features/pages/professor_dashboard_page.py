from selenium.webdriver.common.by import By
from features import Browser


class ProfessorDashboardPageLocator(object):
    # Login page elements locator
    URL = '/professor/dashboard/'


class ProfessorDashboardPage(Browser):
    def navigate(self, base_url):
        self.driver.get(base_url + ProfessorDashboardPageLocator.URL)

    # Login page actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()