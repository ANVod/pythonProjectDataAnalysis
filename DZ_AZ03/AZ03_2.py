#2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.​
#import numpy as np
#random_array = np.random.rand(5) # массив из 5 случайных чисел
#print(random_array)

import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 100  # Количество точек
x_data = np.random.rand(num_points)  # Набор случайных чисел для оси X
y_data = np.random.rand(num_points)  # Набор случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.scatter(x_data, y_data, color='blue', alpha=0.5, edgecolor='black')

# Добавление заголовков и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')

# Отображение диаграммы
plt.show()