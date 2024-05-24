from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page_calculator import Calculator

# Установка и запуск драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_calculator():
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    calculator = Calculator(driver)
    calculator.delay()
    calculator.sum_nums()
    assert calculator.result() == '15'
    
    calculator.close_driver()