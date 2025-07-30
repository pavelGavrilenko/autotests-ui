import re

from playwright.sync_api import Page, expect

from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.reg_form = RegistrationFormComponent(page)
        self.reg_button = Button(page,"registration-page-registration-button","registration")
        self.login_link = Link(page, "registration-page-login-link", "login")



    def click_reg_button(self):
        self.reg_button.click()

    def click_login_link(self):
        self.login_link.click()
        # Добавили проверку
        self.check_current_url(re.compile(".*/#/auth/login"))
