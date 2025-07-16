import pytest
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page):

    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email = chromium_page.get_by_test_id("login-form-email-input").locator("input")
    email.fill('user.name@gmail.com')

    password = chromium_page.get_by_test_id("login-form-password-input").locator("input")
    password.fill('Password')

    login_button = chromium_page.get_by_test_id("login-page-login-button")
    login_button.click()

    alert_login = chromium_page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(alert_login).to_be_visible()
    expect(alert_login).to_have_text('Wrong email or password')