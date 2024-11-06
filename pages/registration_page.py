import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.shadowroot import ShadowRoot
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from pages.base_page import BasePage
from tests.conftest import driver


class RegistrationPage(BasePage):
    URL = 'https://koshelek.ru/authorization/signup'

    shadow_root_selector = ".remoteComponent"
    username_selector = 'div[data-wi="user-name"] input'
    email_selector = '#username'
    password_selector = '#new-password'
    referral_code_selector = 'div[data-wi="referral"] input'
    submit_button_selector = 'div[data-wi="submit-button"] button'
    consent_checkbox_selector = 'div[data-wi="user-agreement"] input[type="checkbox"]'
    full_form_selector = 'div[data-wi="content"]'
    captcha_selector = 'div.hcaptcha-logo[title="hCaptcha"]'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def loginByUsernameEmailAndPassword(self, username, email, password):
        self.fillUsername(username)
        self.fillEmail(email)
        self.fillPassword(password)
        self.setConsentCheckbox(True)

    def _get_shadow_root(self) -> ShadowRoot:
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.shadow_root_selector)))
        shadow_root = self.driver.find_element(By.CSS_SELECTOR, self.shadow_root_selector).shadow_root
        return shadow_root

    def fillUsername(self, username):
        shadow_root = self._get_shadow_root()
        username_field = shadow_root.find_element(By.CSS_SELECTOR, self.username_selector)
        username_field.send_keys(username)

    def fillEmail(self, email):
        shadow_root = self._get_shadow_root()
        email_field = shadow_root.find_element(By.CSS_SELECTOR, self.email_selector)
        email_field.send_keys(email)

    def fillPassword(self, password):
        shadow_root = self._get_shadow_root()
        password_field = shadow_root.find_element(By.CSS_SELECTOR, self.password_selector)
        password_field.send_keys(password)

    def fillReferralCode(self, code):
        shadow_root = self._get_shadow_root()
        code_field = shadow_root.find_element(By.CSS_SELECTOR, self.referral_code_selector)
        code_field.send_keys(code)

    def setConsentCheckbox(self, is_enabled):
        shadow_root = self._get_shadow_root()
        checkbox = shadow_root.find_element(By.CSS_SELECTOR, self.consent_checkbox_selector)
        if checkbox.is_selected() != is_enabled:
            checkbox.click()

    def clickForwardButton(self):
        shadow_root = self._get_shadow_root()
        button = shadow_root.find_element(By.CSS_SELECTOR, self.submit_button_selector)
        button.click()

    def check_if_page_is_open(self):
        assert self.driver.current_url == self.URL, f"URL = {self.driver.current_url} вместо {self.URL}"
        shadow_root = self._get_shadow_root()
        username_field = shadow_root.find_element(By.CSS_SELECTOR, self.username_selector)
        assert username_field.is_displayed(), "Форма регистрации не видна"

    def check_if_text_is_present_on_registration_form(self, text):
        shadow_root = self._get_shadow_root()
        full_content = shadow_root.find_element(By.CSS_SELECTOR, self.full_form_selector)
        assert text in full_content.text, f"На форме авторизации не отображается текст '{text}'"

    def check_captcha_is_not_shown(self):
        captcha_logo = self.driver.find_elements(By.CSS_SELECTOR, self.captcha_selector)
        assert len(captcha_logo) == 0, "Некорректный переход на страницу с капчей"
