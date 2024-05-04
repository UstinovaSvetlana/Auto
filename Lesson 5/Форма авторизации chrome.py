from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Зайди на сайт
driver.get("http://the-internet.herokuapp.com/login")

# В поле username введите значение tomsmith
user_name_field = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
user_name_field.send_keys("tomsmith")

# В поле password введите значение SuperSecretPassword!
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
input_password_field.send_keys("SuperSecretPassword!")

# Нажми кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, 'button[class="radius"]')
login_button.click()

sleep(5)
driver.quit()