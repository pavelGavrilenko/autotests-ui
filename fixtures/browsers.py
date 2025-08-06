######## Browsers without trace and cast
# import pytest
# from playwright.sync_api import Playwright
#
# from pages.authentication.registration_page import RegistrationPage
#
#
# @pytest.fixture
# def chromium_page(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     yield browser.new_page()
#     browser.close()
#
#
# @pytest.fixture(scope="session")
# def initialize_browser_state(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#
#     registration_page = RegistrationPage(page=page)
#     registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
#     registration_page.reg_form.fill(email='user.name@gmail.com', username='username', password='password')
#     registration_page.click_reg_button()
#
#     context.storage_state(path="browser-state.json")
#     browser.close()
#
#
# @pytest.fixture
# def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(storage_state="browser-state.json")
#     yield context.new_page()
#     browser.close()


######## Browsers with trace + video + attach to alure
import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page

@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright):
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.reg_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_reg_button()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright):
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state="browser-state.json"
    )