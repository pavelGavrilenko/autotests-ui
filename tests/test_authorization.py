from playwright.sync_api import sync_playwright, expect

def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:
        bro = playwright.chromium.launch(headless=False)
        page = bro.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email = page.get_by_test_id("login-form-email-input").locator("input")
        email.fill('user.name@gmail.com')

        password = page.get_by_test_id("login-form-password-input").locator("input")
        password.fill('Password')

        login_button = page.get_by_test_id("login-page-login-button")
        login_button.click()

        alert_login = page.get_by_test_id("login-page-wrong-email-or-password-alert")
        expect(alert_login).to_be_visible()
        expect(alert_login).to_have_text('Wrong email or password')