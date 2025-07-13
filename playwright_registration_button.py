from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    bro = playwright.chromium.launch(headless=False)
    page = bro.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    reg_button = page.get_by_test_id("registration-page-registration-button")
    expect(reg_button).to_be_disabled()

    email = page.get_by_test_id("registration-form-email-input").locator("input")
    email.fill('user.name@gmail.com')

    username = page.get_by_test_id("registration-form-username-input").locator("input")
    username.fill('username')

    password = page.get_by_test_id("registration-form-password-input").locator("input")
    password.fill('password')


    expect(reg_button).to_be_enabled()