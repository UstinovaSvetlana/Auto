from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)

    def personal_data(self, first_name: str, last_name: str, address: str, email: str, phone: str, city: str, country: str, job_position: str, company: str) -> None:
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)
        self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').clear()
        sleep(5)
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        sleep(5)

    def get_zip_code_color(self) -> str:
        return self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').value_of_css_property('background-color')

    def get_other_fields_colors(self) -> list[str]:
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']
        colors = [self._driver.find_element(By.CSS_SELECTOR, f'[name="{field}"]').value_of_css_property('background-color') for field in fields]
        return colors

    def close_driver(self) -> None:
        self._driver.quit()