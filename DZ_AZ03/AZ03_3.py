from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

# Настройка драйвера для Firefox
driver = webdriver.Firefox()

# URL страницы
url = 'https://www.divan.ru/category/pramye-divany'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(10)

# Прокрутка страницы вниз для загрузки всех элементов (ограничено 5 итерациями)
max_scrolls = 5
for _ in range(max_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)  # Ждем некоторое время для загрузки новых данных

# Парсинг цен
prices_elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='price']")

# Извлечение текста цен и преобразование их в числа
prices = []
for price_element in prices_elements:
    price_text = price_element.text.replace(" ", "").replace("₽", "").strip()
    if price_text.isdigit():
        prices.append(int(price_text))

# Проверка, что цены были найдены
if not prices:
    print("Цены не были найдены. Проверьте правильность селекторов.")
else:
    # Открытие CSV файла для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Записываем заголовок столбца

        # Записываем цены в CSV файл
        for price in prices:
            writer.writerow([price])

    # Расчет средней цены
    average_price = np.mean(prices)
    print(f'Средняя цена на диваны: {average_price:.2f} ₽')

    # Построение гистограммы цен
    plt.hist(prices, bins=20, edgecolor='k')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()

# Закрытие драйвера
driver.quit()