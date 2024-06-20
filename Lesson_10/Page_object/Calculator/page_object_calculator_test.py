import allure
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page_calculator import Calculator

@allure.title("Калькулятор")
@allure.description("Проверка работы калькулятора")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_calculator():
    """
    Тестовый сценарий для проверки работы калькулятора на веб-странице.
    """
    with allure.step("Запуск браузера Chrome"):
        # Инициализация и запуск браузера Chrome
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Загрузка страницы калькулятора"):
        # Переход на страницу калькулятора
        calculator = Calculator(driver)

    with allure.step("Выставление задержки выполнения действия"):
        # Установка задержки выполнения действий (опционально)
        calculator.delay()

    with allure.step("Выполнение выражения"):
        # Выполнение вычисления (например, суммы чисел)
        calculator.sum_nums()

    with allure.step("Сравнение значения выражения с числом 15"):
        # Проверка, что результат вычисления равен 15
        assert calculator.result() == '15', f"Expected result to be '15' but got '{calculator.result()}'"
        
    with allure.step("Закрытие браузера Chrome"):
        # Закрытие браузера
        calculator.close_driver()
