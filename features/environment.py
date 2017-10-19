from browser import Browser
from selenium import webdriver


def before_all(context):

    # PhantomJS is used there (headless browser - meaning we can execute tests in a command-line environment,
    # which is what we want for use with SemaphoreCI
    # For debugging purposes, you can use the Firefox driver instead.
    context.browser = webdriver.PhantomJS()
    # Small unit of wait between instructions, allowing things to load
    context.browser.implicitly_wait(1)
    # Screen size must be wide enough to let PhantomJS find elements
    context.browser.set_window_size(1920, 1080)
    # Using a different port, not conflicting if server is booted up
    context.server_url = 'http://localhost:8080'


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.browser.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass
