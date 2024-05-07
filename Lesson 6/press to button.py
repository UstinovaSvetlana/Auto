from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Настройка драйвера на ожидание
driver.implicitly_wait(17)

# Зайди на сайт, найди  "синию кнопку" и кликни на нее
driver.get("http://uitestingplayground.com/ajax")
blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()


# Найди появившийся элемент и выведи в консоль текст на элементе
data = driver.find_element(By.CSS_SELECTOR, 'p[class="bg-success"]').text
print(data)

# Закрой браузер
driver.quit()