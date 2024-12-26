from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()
driver.get("http://0.0.0.0:8000/html_pages/elements.html")

# Знаходження текстових полів за ID і введення тексту
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("example_username")

print(username_field.get_attribute('value'))  # надрукує нам цей текст


password_field = driver.find_element(By.ID, "password")
password_field.send_keys("example_password")

# Знаходження радіо кнопок за ID і вибір варіанта
male_radio = driver.find_element(By.ID, "male")
male_radio.click()

# male_radio.is_selected()

# Знаходження чекбоксу за ID і встановлення прапорця
newsletter_checkbox = driver.find_element(By.ID, "newsletter")
newsletter_checkbox.click()

# Вибір значення з випадаючого списку за ID
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("США")

# Натискання на кнопку за ID
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

# Зачекати 5 секунд перед завершенням
time.sleep(5)

# Закрити браузер
driver.quit()