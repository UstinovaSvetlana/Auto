from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from buying_page import BuyingPage

def test_buying_process():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    page = BuyingPage(browser)
    
    page.authorization("standard_user", "secret_sauce")
    page.add_products()
    page.go_to_cart()
    page.personal_data("Sveta", "Ustinova", "123456")
    total = page.total_cost()
    assert total == "Total: $58.29", f"Expected total to be 'Total: $58.29' but got '{total}'"
    
    page.close()

test_buying_process()