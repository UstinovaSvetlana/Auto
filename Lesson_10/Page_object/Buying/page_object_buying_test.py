import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from buying_page import BuyingPage

@allure.title("Проверка итоговой стоимости в интернет-магазине")
@allure.description("Тест сравнивает сумму добавленных в корзину товаров с конкретным значением")
@allure.feature("CREATE")
@allure.severity("blocker")

def test_buying_process():
    with allure.step("Запуск браузера Chrome"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Переход на страницу интернет-магазина"):
        page = BuyingPage(browser)

    with allure.step("Авторизация"):
        page.authorization("standard_user", "secret_sauce")
    
    with allure.step("Добавление товаров в корзину"):
        page.add_products()
    
    with allure.step("Переход в корзину"):
        page.go_to_cart()

    with allure.step("Ввод данных покупателя"):
        page.personal_data("Света", "Устинова", "123456")
    
    with allure.step("Сравнение итоговой стоимости с конкретным значением"):
        total = page.total_cost()
    assert total == "Total: $58.29", f"Expected total to be 'Total: $58.29' but got '{total}'"
    
    page.close()