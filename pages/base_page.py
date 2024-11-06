from selenium.webdriver.chrome.webdriver import WebDriver

from tests.conftest import driver


class BasePage:
    URL=""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)