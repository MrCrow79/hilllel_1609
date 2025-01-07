import pytest
from selenium.webdriver import Chrome

from core.ui.sausedemo.pages.login_page import LoginPage
from settings import settings


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()


@pytest.fixture  # scope = function by default
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.check_is_correct_url()
    return login_page


@pytest.fixture(scope='session')
def driver_session():
    driver = Chrome()
    yield driver
    driver.close()


@pytest.fixture(scope='session')
def login_page_session(driver_session):
    login_page = LoginPage(driver_session)
    login_page.open_page()
    login_page.check_is_correct_url()
    return login_page

@pytest.fixture(scope='session')
def product_page_session(login_page_session):
    return login_page_session.login_user(settings.saucedemo_user, settings.saucedemo_pwd)