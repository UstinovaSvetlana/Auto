from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)

    def delay(self):
        delay_field = self._driver.find_element(By.CSS_SELECTOR, 'input[id = "delay"]')
        delay_field.clear()
        delay_field.send_keys('2')

    def sum_nums(self):
        self._driver.find_element(By.XPATH, '//span[contains(text(),"7")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"+")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"8")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"=")]').click()
    def result(self):
        wait = WebDriverWait(self._driver, 4)
        wait.until(EC. text_to_be_present_in_element((By.CSS_SELECTOR, '[class = "screen"]'), '15'))
        return self._driver.find_element(By.CSS_SELECTOR, '[class = "screen"]').text

    def close_driver(self):
        self._driver.quit()
        