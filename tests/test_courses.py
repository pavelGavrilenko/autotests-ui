import pytest
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    course_in_navbar = chromium_page_with_state.get_by_test_id("courses-drawer-list-item-button")
    expect(course_in_navbar.locator("span")).to_have_text("Courses")

    text_nothing_in_list = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_nothing_in_list).to_have_text("Results from the load test pipeline will be displayed here")
