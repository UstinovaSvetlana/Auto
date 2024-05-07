from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Зайди на сайт, найди  "синию кнопку" и кликни на нее
driver.get("http://uitestingplayground.com/textinput")

# Найди поле ввода
input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')

# Очисти поле ввода перед вводом и введи текст "SkyPro"
input_field.clear()
input_field.send_keys("SkyPro")

# Найди синюю кнопку и кликни на нее
rename_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
rename_button.click()

# Выдели текст кнопки и выведите в консоль (SkyPro)
new_name = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').text
print(new_name)

# Закрой браузер
driver.quit()