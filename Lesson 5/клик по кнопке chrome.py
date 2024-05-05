from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


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

sleep(5)
driver.quit()