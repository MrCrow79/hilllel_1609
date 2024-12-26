from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()

driver.get("http://0.0.0.0:8000/html_pages/demo.html")  # open new tab with "http://localhost:8000/demo.html" page


# Знаходження елемента за ID
user_field = driver.find_element(By.ID, "username")  # By.CSS_SELECTOR #username
pass_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")

# Знаходження елемента за XPath з вказанням значення
li_el2 = driver.find_element(By.XPATH, "//li[.='Елемент списку 2']")

# Знаходження елемента за XPath з вказанням iндексу
li_el2_idx = driver.find_element(By.XPATH, "//li[2]")

li_el = driver.find_element(By.XPATH, "//li")

li_elements = driver.find_elements(By.TAG_NAME, "li")

# Пошук конкретного елемента серед отриманих
for li in li_elements:
    # пошук може бути повiльним якщо елементiв багато
    if li.text == "Елемент списку 2":
        # Знайдено потрібний елемент
        print("Знайдено елемент:", li.text)
        break