import time

import pytest

from pages.registration_page import RegistrationPage


# предусловие для теста: в базу данных добавлен пользователь с именем username
def test_cannot_signup_with_existing_username(driver):
    page = RegistrationPage(driver)
    page.open()
    page.loginByUsernameEmailAndPassword("username",
                                         "something18943@company.net",
                                         "Password498321")
    page.check_if_page_is_open()
    page.check_if_text_is_present_on_registration_form( "Имя пользователя уже занято")


def test_cannot_signup_without_consent_checkbox_checked(driver):
    page = RegistrationPage(driver)
    page.open()
    page.loginByUsernameEmailAndPassword("username5364",
                                         "something18943@company.net",
                                         "Password498321")
    page.clickForwardButton()
    page.check_if_page_is_open()
    page.check_captcha_is_not_shown()


@pytest.mark.parametrize("username, email, password",
                         [("user123573", "email@company.net", ""),
                          ("user123573", "", "password"),
                          ("", "email@company.net", "password")])
def test_registration_fields_are_required(driver, username, email, password):
    page = RegistrationPage(driver)
    page.open()
    page.loginByUsernameEmailAndPassword(username, email, password)
    page.clickForwardButton()
    page.check_if_page_is_open()
    page.check_if_text_is_present_on_registration_form("Поле не заполнено")


# в настоящее время на сайте нет ограничения на максимальную длину поля email
@pytest.mark.parametrize("username, email, password, referral_code, expected_message",
                         [("a" * 33, "email@company.net", "Password123", "", "Допустимые символы (от 6 до 32)"),
                          ("user123573", "email@company.net", "x" * 65, "", "Пароль должен содержать от 8 до 64 символов"),
                          ("user123573", "email@company.net", "Password123", "123456789", "Неверный формат ссылки")])
def test_registration_fields_have_maximal_length(driver, username, email, password, referral_code, expected_message):
    page = RegistrationPage(driver)
    page.open()
    page.loginByUsernameEmailAndPassword(username, email, password)
    page.fillReferralCode(referral_code)
    page.check_if_text_is_present_on_registration_form(expected_message)


@pytest.mark.parametrize("username, email, password, referral_code, expected_message",
                         [("abcde", "email@company.net", "Password123", "", "Допустимые символы (от 6 до 32)"),
                          ("user123573", "email@company.net", "1234567", "", "Пароль должен содержать минимум 8 символов"),
                          ("user123573", "email@company.net", "Password123", "123", "Неверный формат ссылки")])
def test_registration_fields_have_minimal_length(driver, username, email, password,referral_code, expected_message):
    page = RegistrationPage(driver)
    page.open()
    page.loginByUsernameEmailAndPassword(username, email, password)
    page.fillReferralCode(referral_code)
    page.check_if_text_is_present_on_registration_form(expected_message)


def test_username_should_begin_with_a_letter(driver):
    page = RegistrationPage(driver)
    page.open()
    page.loginByUsernameEmailAndPassword("1player", "username@company.net", "Password123")
    page.check_if_text_is_present_on_registration_form("Имя должно начинаться с буквы")


def test_username_field_has_symbol_requirements(driver):
    page = RegistrationPage(driver)
    page.open()
    page.loginByUsernameEmailAndPassword("Useruser'", "username@company.net", "Password123")
    page.check_if_text_is_present_on_registration_form("Допустимые символы (от 6 до 32): a-z, 0-9, _.")


def test_email_field_has_format_requirements(driver):
    page = RegistrationPage(driver)
    page.open()
    page.fillEmail("somethingsomething.com")
    page.clickForwardButton()
    page.check_if_text_is_present_on_registration_form("Формат e-mail: username@test.ru")


@pytest.mark.parametrize("password", ["ALLUPPERCASEAND123", "alllowercaseand123", "uppercaseANDlowercase"])
def test_password_field_should_contain_uppercase_lowercase_and_digits(driver, password):
    page = RegistrationPage(driver)
    page.open()
    page.fillPassword(password)
    page.clickForwardButton()
    page.check_if_text_is_present_on_registration_form(
        "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры")
