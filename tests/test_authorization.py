import pytest
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(
        chromium_page,
        email: str,
        password: str
):

    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id("login-form-email-input").locator("input")
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id("login-form-password-input").locator("input")
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id("login-page-login-button")
    login_button.click()

    alert_login = chromium_page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(alert_login).to_be_visible()
    expect(alert_login).to_have_text('Wrong email or password')