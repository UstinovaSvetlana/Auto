from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Зайди на сайт
driver.get("http://the-internet.herokuapp.com/inputs")

# Введи в поле 1000
input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys("1000")

# Очисти это поле (метод clear)
input_field.clear()

# Введи в это же поле  999
input_field.send_keys("999")

driver.quit()