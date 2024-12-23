from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep

webdriver = WebDriver()

webdriver.get('https://www.saucedemo.com')

sleep(1)
user_name = webdriver.find_element(By.ID, value='user-name').send_keys('standard_user')
sleep(2)
webdriver.find_element(By.ID, value='password').send_keys('secret_sauce')
sleep(2)
webdriver.find_element(by=By.XPATH, value='//input[@data-test="login-button"]').click() #
sleep(2)

# open_login_page()
# fill_user_name_and_password()
# login()
# check_user_was_logged_in()