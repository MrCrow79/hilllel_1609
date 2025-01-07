from core.ui.sausedemo.locators.product_page import ProductPageLocators
from core.ui.sausedemo.pages.base_page import BasePage
from settings import settings


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = f'{settings.saucedemo_url}inventory.html'
        self.locators = ProductPageLocators()

        self.default_sorting_text = 'Name (A to Z)'
        self.is_default_sorting_reversed = False


    def image_of_product(self):
        return self._present_element(self.locators.image_of_product)


    def get_dropdown_option_by_text(self, text, dropdown):
        option_inside_dropdown = dropdown.find_elements('xpath', '//option')
        # TODO: add check that we have only 1 element
        return [k for k in option_inside_dropdown if k.text == text][0]


    def get_current_sorting_element(self):

        return self.get_dropdown_option_by_text(
            text=self._present_element(self.locators.active_option_span).text,
            dropdown=self._present_element(self.locators.sorting_select))


    def select_sorting(self, name):
        dropdown = self._present_element(self.locators.sorting_select)

        option_to_select = self.get_dropdown_option_by_text(
            text=name,
            dropdown=dropdown)

        dropdown.click()
        option_to_select.click()

        return self


    def products(self):
        return self._present_elements(self.locators.product_item)


    def products_names(self):
        return self._present_elements(self.locators.name_of_product)


    def products_prices(self):
        return self._present_elements(self.locators.price_of_product)