from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Зайди на сайт, найди кнопку "синию кнопку" и кликни на нее
for _ in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    button_with_dynamic_id = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    button_with_dynamic_id.click()


sleep(5)
driver.quit()