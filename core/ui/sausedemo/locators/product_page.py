from selenium.webdriver.common.by import By


class ProductPageLocators:
    image_of_product = (By.XPATH, '//div[@class="inventory_item_img"]')
    sorting_select = (By.XPATH, '//select[@class="product_sort_container"]')
    active_option_span = (By.XPATH, '//span[@class="active_option"]')

    product_item = (By.XPATH, '//div[@class="inventory_item"]')
    name_of_product = (By.XPATH, '//div[@class="inventory_item_name "]')
    price_of_product = (By.XPATH, '//div[@class="inventory_item_price"]')
