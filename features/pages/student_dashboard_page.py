from features import Browser


class StudentDashboardPageLocator(object):
    # Login page elements locator
    URL = '/student/dashboard/'


class StudentDashboardPage(Browser):
    def navigate(self, base_url):
        self.driver.get(base_url + StudentDashboardPageLocator.URL)

    # Login page actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def currently_on_this_page(self):
        return self.current_url_endswith(StudentDashboardPageLocator.URL)
