# 2. Определите среднюю зарплату (Salary) по городу (City)
# - используйте файл приложенный к дз - dz.csv​

import pandas as pd

# Загрузка данных из CSV-файла
df = pd.read_csv('dz.csv')

# Группировка данных по городу и расчет средней зарплаты
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод результата
print("Средняя зарплата по городам:")
print(average_salary_by_city)