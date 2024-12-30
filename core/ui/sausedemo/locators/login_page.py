from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_input = (By.ID, 'user-name')
    password_input = (By.ID, 'password')
    login_button = (By.XPATH, '//input[@data-test="login-button"]')
    error_text_element = (By.XPATH, '//h3[@data-test="error"]')
    red_cross = (By.XPATH, '//*[@data-prefix="fas"]')