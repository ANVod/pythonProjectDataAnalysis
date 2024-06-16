import pandas as pd
import re

# Чтение данных из CSV файла
df = pd.read_csv('prices.csv', header=None)

# Функция для обработки каждой строки
def process_price(row):
    # Ищем первую цену в строке
    match = re.search(r'(\d[\d\s]*руб\.)', row)
    if match:
        # Убираем 'руб.' и пробелы, затем конвертируем в число
        clean_price = match.group(1).replace('руб.', '').replace(' ', '')
        return int(clean_price)
    return None

# Новый DataFrame для хранения обработанных данных
processed_prices = []

# Обработка каждой строки
for index, row in df.iterrows():
    price = process_price(' '.join(row.dropna().astype(str)))
    if price is not None:
        processed_prices.append([price])

# Создаем DataFrame из обработанных данных
processed_df = pd.DataFrame(processed_prices, columns=['Price'])

# Записываем обработанные данные обратно в CSV файл
processed_df.to_csv('processed_prices.csv', index=False)

print('Данные обработаны и сохранены в processed_prices.csv')