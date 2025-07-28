from playwright.sync_api import Page, expect

from elements.button import Button
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.reg_form = RegistrationFormComponent(page)
        self.reg_button = Button(page,"registration-page-registration-button","registration")



    def click_reg_button(self):
        self.reg_button.click()