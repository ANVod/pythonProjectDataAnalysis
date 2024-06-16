import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
data = pd.read_csv('processed_prices.csv')

# Предполагая, что столбец с ценами называется 'price'
prices = data['Price']

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=30, edgecolor='k', alpha=0.7)
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(True)

# Показать график
plt.show()