import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.fixture
def chromium_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    bro = playwright.chromium.launch(headless=False)
    context = bro.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email = page.get_by_test_id("registration-form-email-input").locator("input")
    email.fill('user.name@gmail.com')
    username = page.get_by_test_id("registration-form-username-input").locator("input")
    username.fill('username')
    password = page.get_by_test_id("registration-form-password-input").locator("input")
    password.fill('password')
    reg_button = page.get_by_test_id("registration-page-registration-button")
    reg_button.click()
    context.storage_state(path="browser-state.json")
    bro.close()


@pytest.fixture(autouse=True)
def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
    bro = playwright.chromium.launch(headless=False)
    contex = bro.new_context(storage_state="browser-state.json")
    yield contex.new_page()
    bro.close()