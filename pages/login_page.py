from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        email_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_form.send_keys(email)
        pass1_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        pass1_form.send_keys(password)
        pass2_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        pass2_form.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login"), "login word is present in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is present"