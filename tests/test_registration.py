from playwright.sync_api import sync_playwright, expect

def test_successful_registration():
    with sync_playwright() as playwright:
        bro = playwright.chromium.launch(headless=False)
        page = bro.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email = page.get_by_test_id("registration-form-email-input").locator("input")
        email.fill('user.name@gmail.com')

        username = page.get_by_test_id("registration-form-username-input").locator("input")
        username.fill('username')

        password = page.get_by_test_id("registration-form-password-input").locator("input")
        password.fill('password')

        reg_button = page.get_by_test_id("registration-page-registration-button")
        reg_button.click()

        dashbord_tittle = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashbord_tittle).to_be_visible()
        expect(dashbord_tittle).to_have_text('Dashboard')
