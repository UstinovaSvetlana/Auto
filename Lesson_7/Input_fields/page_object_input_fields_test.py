from mainpage_input_fields import MainPage

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_input_fields():
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    mainpaige_input_fields = MainPage(driver)
    mainpaige_input_fields.personal_data("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    
    assert mainpaige_input_fields.zip_code_red() == 'rgba(248, 215, 218, 1)'
    
    assert mainpaige_input_fields.other_fields_green() == 'rgba(209, 231, 221, 1)'

    mainpaige_input_fields.close_driver()