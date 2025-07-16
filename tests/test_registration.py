import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email = chromium_page.get_by_test_id("registration-form-email-input").locator("input")
    email.fill('user.name@gmail.com')

    username = chromium_page.get_by_test_id("registration-form-username-input").locator("input")
    username.fill('username')

    password = chromium_page.get_by_test_id("registration-form-password-input").locator("input")
    password.fill('password')

    reg_button = chromium_page.get_by_test_id("registration-page-registration-button")
    reg_button.click()

    dashbord_tittle = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashbord_tittle).to_be_visible()
    expect(dashbord_tittle).to_have_text('Dashboard')
