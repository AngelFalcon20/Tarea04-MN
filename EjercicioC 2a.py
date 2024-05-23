# Grafica de y=x y y=sinx
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2*np.pi, 2*np.pi, 100)


y1 = x
y2 = np.sin(x)


plt.figure(figsize=(8, 6))

# Gráfica de y = x
plt.plot(x, y1, label="y = x", color="blue")

# Gráfica de y = sin(x)
plt.plot(x, y2, label="y = sin(x)", color="red")

# Etiquetas y título
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráficas de y = x y y = sin(x)")
plt.legend()


plt.grid(True)
plt.show()