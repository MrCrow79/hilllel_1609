from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.ui.sausedemo.locators.product_page import ProductPageLocators
from core.ui.sausedemo.pages.base_page import BasePage
from settings import settings


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = f'{settings.saucedemo_url}/inventory.html'
        self.locators = ProductPageLocators()


    def image_of_product(self):
        return self._present_element(self.locators.image_of_product)