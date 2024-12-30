from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.ui.sausedemo.pages.login_page import LoginPage
from core.ui.sausedemo.pages.product_page import ProductPage
from settings import settings

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

import pytest


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    return login_page


def test_product_page_is_opened(driver, login_page):

    product_page = login_page.login_user(settings.saucedemo_user, settings.saucedemo_pwd)
    product_page.image_of_product()


def test_wrong_user_name(driver, login_page):

    login_page.set_user_name('wrong_user_name').set_user_pwd(settings.saucedemo_pwd).click_login()
    login_page.error_h3_text_wrong_name_or_pwd()
    login_page.check_there_are_3_red_crosses()




