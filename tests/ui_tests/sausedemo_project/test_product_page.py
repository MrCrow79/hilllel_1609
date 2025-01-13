from settings import settings

import pytest
import allure


@allure.feature('UI tests')
@pytest.mark.UI
def test_product_page_is_opened(driver, login_page):

    product_page = login_page.login_user(settings.saucedemo_user, settings.saucedemo_pwd)
    product_page.check_is_correct_url()
    product_page.image_of_product()

@allure.feature('UI tests')
def test_wrong_user_name(driver, login_page):

    login_page.set_user_name('wrong_user_name').set_user_pwd(settings.saucedemo_pwd).click_login()
    login_page.error_h3_text_wrong_name_or_pwd()
    login_page.check_there_are_3_red_crosses()
