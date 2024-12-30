
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.ui.utils.custom_conditions import WaitForNElements


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self.url = None


    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)


    def _present_element(self, locator, message='', timeout=1):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)


    def _present_elements(self, locator, message='', timeout=1):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_all_elements_located(locator), message=message)


    def _wait_for_n_elements_are_presented(self, locator, el_quantity, message='', timeout=5):

        return WebDriverWait(self._driver, timeout).until(WaitForNElements(locator, el_quantity), message=message)


    def _present_text(self, locator, text, message='', timeout=1):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text), message=message)


    def _input_field(self, locator, message='', timeout=1):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)


    def _button(self, locator, message='', timeout=1):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(locator), message=message)