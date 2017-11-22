import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features import Browser


class ClassPageLocator(object):
    # Login page elements locator
    URL = r'/professor/lesson/[0-9]+'


class ClassPage(Browser):
    def navigate(self, base_url):
        pass

    def currently_on_this_page(self):
        return re.search(ClassPageLocator.URL, self.driver.current_url)

    # Login page actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def select(self, text, *locator):
        Select(self.driver.find_element(*locator)).select_by_value(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()
