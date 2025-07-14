from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
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
        dashbord_tittle = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashbord_tittle).to_be_visible()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright_2:
        bro_2 = playwright_2.chromium.launch(headless=False)
        context_2 = bro_2.new_context(storage_state="browser-state.json")
        page_2 = context_2.new_page()

        page_2.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        course_in_navbar = page_2.get_by_test_id("courses-drawer-list-item-button")
        expect(course_in_navbar.locator("span")).to_have_text("Courses")

        text_nothing_in_list = page_2.get_by_test_id("courses-list-empty-view-description-text")
        expect(text_nothing_in_list).to_have_text("Results from the load test pipeline will be displayed here")
