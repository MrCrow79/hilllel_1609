from selenium.webdriver.common.by import By

from core.ui.sausedemo.locators.login_page import LoginPageLocators
from core.ui.sausedemo.pages.base_page import BasePage
from core.ui.sausedemo.pages.product_page import ProductPage
from settings import settings
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = settings.saucedemo_url
        self.locators = LoginPageLocators()

    @allure.step('Search user name input')
    def _username_input(self):
        return self._input_field(self.locators.username_input, message='Cant find user name input at Login Page',
                                 timeout=3)

    @allure.step('Search user pwd input')
    def _user_pwd_input(self):
        return self._input_field(self.locators.password_input, message='Cant find user pwd input at Login Page')

    @allure.step('Search login button ')
    def _login_button(self):
        return self._button(self.locators.login_button, message='Cant find login button at Login Page', timeout=4)


    def error_h3_text_wrong_name_or_pwd(self):
        return self._present_text(self.locators.error_text_element,
                                  'Epic sadface: Username and password do not match any user in this service',
                                  message='Cant find specific error text', timeout=10)

    def error_crosses(self):
        return self._present_elements(self.locators.red_cross)

    @allure.step('Search 3 red crosses')
    def check_there_are_3_red_crosses(self):
        expected_crosses = 3
        self._wait_for_n_elements_are_presented(locator=self.locators.red_cross, el_quantity=expected_crosses,
                                                message=f'Looking for red crosses. Expected {expected_crosses}')

    @allure.step('Set value into username field')
    def set_user_name(self, user_name):
        self._username_input().send_keys(user_name)
        return self

    @allure.step('Set value into pwd field')
    def set_user_pwd(self, user_pwd):
        self._user_pwd_input().send_keys(user_pwd)
        return self

    @allure.step('Click login button')
    def click_login(self):
        self._login_button().click()
        return self


    # positive_cases
    @allure.step('Login {user_name} user')
    def login_user(self, user_name, user_pwd) -> ProductPage:
        self.set_user_name(user_name).set_user_pwd(user_pwd).click_login()
        return ProductPage(self._driver)