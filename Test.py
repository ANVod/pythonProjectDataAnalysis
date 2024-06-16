from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Создаем экземпляр браузера Firefox
driver = webdriver.Firefox()

# URL страницы
url = 'https://www.divan.ru/category/pramye-divany'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Прокрутите страницу вниз, чтобы загрузить все элементы (если необходимо)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.CSS_SELECTOR, '.lsooF')

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()

print('Цены сохранены в prices.csv')