import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.title("График функции y = x**2")
plt.grid(True)
plt.show()