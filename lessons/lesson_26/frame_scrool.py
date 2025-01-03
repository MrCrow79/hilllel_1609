from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ініціалізуємо драйвер Chrome
driver = webdriver.Chrome()

# Відкриваємо головну сторінку
driver.get("http://0.0.0.0:8000/html_pages/scroll_frame.html")
time.sleep(1)

# driver.switch_to.frame(driver.find_element(By.ID, "myFrame"))
# Прокрутка вниз
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # виконання js
time.sleep(1)  # Зачекайте трохи після прокрутки вниз

# Прокрутка вгору
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)  # Зачекайте трохи після прокрутки вгору

# Перемикаємося до фрейму
driver.switch_to.frame(driver.find_element(By.ID, "myFrame"))

# Натискання на кнопку три рази
for _ in range(3):
    button = driver.find_element(By.ID, "myButton")
    button.click()
    time.sleep(1)  # Зачекайте трохи після кожного натискання

# Закриваємо браузер
driver.quit()