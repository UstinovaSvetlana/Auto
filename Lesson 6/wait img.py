from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Настройка драйвера на ожидание
driver.implicitly_wait(12)

# Зайди на сайт, найди  "синию кнопку" и кликни на нее
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


# Найди появившийся элемент и выведи в консоль текст на элементе
src = driver.find_element(By.CSS_SELECTOR, 'img[alt = "award"]').get_attribute("src")
print(src)

# Закрой браузер
driver.quit()