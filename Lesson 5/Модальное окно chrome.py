from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Зайди на сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(10)

# Найди кнопку "close" и кликни на нее
close_button = driver.find_element(By.XPATH, '//p[text()="Close"]')
close_button.click()
sleep(3)

driver.quit()