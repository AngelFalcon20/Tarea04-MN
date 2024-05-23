# Gráfica de y = x - 1 y y = e^x
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)

y1 = x - 1
y2 = np.exp(x)

x += 0.0001234

plt.figure(figsize=(8, 6))

# Gráfica de y = x - 1
plt.plot(x, y1, label="y = x - 1", color="blue")

# Gráfica de y = e^x
plt.plot(x, y2, label="y = e^x", color="red")

# Etiquetas y título
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráficas de y = x - 1 y y = e^x con valor aleatorio añadido a x")
plt.legend()

plt.grid(True)
plt.show()