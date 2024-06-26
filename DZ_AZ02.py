import pandas as pd

# Создание датафрейма с данными
data = {
    'Ученик': ['Ученик1', 'Ученик2', 'Ученик3', 'Ученик4', 'Ученик5',
               'Ученик6', 'Ученик7', 'Ученик8', 'Ученик9', 'Ученик10'],
    'Математика': [85, 78, 92, 68, 90, 75, 80, 89, 77, 95],
    'Физика': [88, 76, 85, 90, 95, 80, 70, 88, 84, 91],
    'Химия': [90, 85, 80, 70, 88, 76, 82, 89, 77, 84],
    'Биология': [85, 90, 88, 76, 82, 80, 78, 91, 84, 87],
    'История': [78, 85, 90, 82, 87, 88, 75, 80, 92, 86]
}

df = pd.DataFrame(data)

# Вывод DataFrame
print(df)

# Вывод первых нескольких строк DataFrame
print(df.head())

# Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("Средние оценки по каждому предмету:\n", mean_scores)

# Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("Медианные оценки по каждому предмету:\n", median_scores)

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"Q1 для оценок по математике: {Q1_math}")
print(f"Q3 для оценок по математике: {Q3_math}")

# Вычисление IQR (межквартильный размах)
IQR_math = Q3_math - Q1_math
print(f"IQR для оценок по математике: {IQR_math}")

# Вычисление стандартного отклонения
std_deviation = df.std(numeric_only=True)
print("Стандартное отклонение по каждому предмету:\n", std_deviation)