from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BuyingPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)

    def authorization(self, name, password):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def add_products(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        counter = 'Total: $58.29'
        return counter

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self._driver.find_element(By.ID, "checkout").click()

    def personal_data(self, name, last_name, postal_code):
        self._driver.find_element(By.ID, "first-name").send_keys(name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.ID, "continue").click()

    def total_cost(self):
        txt = WebDriverWait(self._driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.summary_total_label'))).text
        return txt

    def close(self):
        self._driver.find_element(By.ID, "finish").click()
        self._driver.quit()