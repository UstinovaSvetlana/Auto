import allure
from mainpage_input_fields import MainPage

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Поля ввода")
@allure.description("Тест проверяет, что фон незаполненного поля ввода при попытке перейти на следующую страницу красный")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_input_fields() -> None:
    with allure.step("Запуск браузера Chrome, переход на страницу с полями ввода"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        mainpage_input_fields = MainPage(driver)

    with allure.step("Заполнение полей ввода"):
        mainpage_input_fields.personal_data("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
        
    with allure.step("Проверка: фон заполненных полей зеленый, незаполненного - красный"):
        assert mainpage_input_fields.get_zip_code_color() == 'rgba(248, 215, 218, 1)'
        
        for color in mainpage_input_fields.get_other_fields_colors():
            assert color == 'rgba(209, 231, 221, 1)'

    with allure.step("Закрытие браузера Chrome"):
        mainpage_input_fields.close_driver()