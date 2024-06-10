import pandas as pd


df = pd.read_csv('dz.csv')


average_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод результата
print("Средняя зарплата по городам:")
print(average_salary_by_city)