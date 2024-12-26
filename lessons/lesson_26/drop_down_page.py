import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# iніціалізуємо веб-драйвер
driver = Chrome()

# відкриття сторінки
driver.get("http://0.0.0.0:8000/html_pages/drop_down.html")

# cтворюємо екземпляр класу ActionChains
actions = ActionChains(driver)

# знайти кнопку "Menu"
time.sleep(1)
menu_button = driver.find_element(By.TAG_NAME, "button")

# навести курсор на кнопку "Menu", щоб відобразити випадаюче меню
actions.move_to_element(menu_button).perform()

# знайти всі посилання на продукти в меню "Products"
product_links = driver.find_elements(By.CSS_SELECTOR, ".dropdown-submenu .dropdown-content .product-link")

# пройтися по кожному посиланню і натиснути його
for link in product_links:
    actions.move_to_element(link).perform()
    actions.click(link).perform()
    time.sleep(1)

    # почекати, поки з'явиться діалогове вікно підтвердження
    WebDriverWait(driver, 5).until(EC.alert_is_present())

    time.sleep(1)
    # підтвердити діалогове вікно
    alert = driver.switch_to.alert
    alert.accept()

# закриття веб-драйвера
driver.quit()