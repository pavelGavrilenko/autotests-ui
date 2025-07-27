from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.reg_form = RegistrationFormComponent(page)
        self.reg_button = page.get_by_test_id("registration-page-registration-button")



    def click_reg_button(self):
        self.reg_button.click()