from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, browser, url, timeout = 3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def go_to_login_page(self):
        go_to_login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        go_to_login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"