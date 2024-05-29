from selenium.webdriver.common.by import By
from time import sleep

class MainPage:

# Установка и запуск драйвера Chrome, переход на страницу

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)

    def personal_data(self, name, last, address, email, phone, city, country, job, company):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "first-name"]').send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "last-name"]').send_keys(last)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "address"]').send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "e-mail"]').send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "phone"]').send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "zip-code"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "city"]').send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "country"]').send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "job-position"]').send_keys(job)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "company"]').send_keys(company)
        
        sleep(2)
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
       

    def zip_code_red(self):
        zip_code_color = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return zip_code_color

    def other_fields_green(self):
        other_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                        "#phone", "#city", "#country", "#job-position", "#company"]
        for field in other_fields:
            field_color = self._driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color") 
        return field_color

    def close_driver(self):
        self._driver.quit()