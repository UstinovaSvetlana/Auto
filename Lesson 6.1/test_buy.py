import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def test_byuing():
# Зайди на сайт
    driver.get("https://www.saucedemo.com/")

# В поле username  введи значение 'standard_user'
    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("standard_user")

# В поле password введи значение 'secret_sauce'
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("secret_sauce")

    sleep(2)
# Нажми кнопку Login
    driver.find_element(By.ID,"login-button").click()


# Добавь товары в корзину
    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()

# Перейди в корзину
    driver.find_element(By.XPATH, "//html/body/div/div/div/div[1]/div[1]/div[3]/a").click()

# Нажми checkout
    driver.find_element(By.XPATH, "//*[@id='checkout']").click()

# Введи данные покупателя
    first_name = driver.find_element(By.ID, "first-name").clear()
    first_name = driver.find_element(By.ID, "first-name").send_keys("Sveta")
    last_name = driver.find_element(By.ID, "last-name").clear()
    last_name = driver.find_element(By.ID, "last-name").send_keys("Ustinova")
    zip_code = driver.find_element(By.ID, "postal-code").clear()
    zip_code = driver.find_element(By.ID, "postal-code").send_keys("123456")


# Нажми кнопку Continue
    continue_button = driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()

    total = driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
    print(total)

    sleep(3)

    assert total == "Total: $58.29"

driver.quit()