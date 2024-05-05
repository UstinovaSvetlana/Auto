from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Зайди на сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")  

# Найди кнопку "Add Element" и кликни на нее 5 раз
for _ in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add_button.click()

# Собери список кнопок "Delete"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')

# Выведи размер списка кнопок "Delete"
print("Размер списка кнопок 'Delete':", len(delete_buttons))

driver.quit()