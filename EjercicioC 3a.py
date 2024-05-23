# Gráfica de y = x  y  y = tan(x)
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)

y1 = x
y2 = np.tan(x)

plt.figure(figsize=(8, 6))

# Gráfica de y = x
plt.plot(x, y1, label="y = x", color="blue")

# Gráfica de y = tan(x)
plt.plot(x, y2, label="y = tan(x)", color="red")


plt.ylim(-10, 10)
plt.xlim(-2*np.pi, 2*np.pi)
plt.gca().set_aspect("equal", adjustable="box")

# Etiquetas y título
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráficas de y = x y y = tan(x)")
plt.legend()

plt.grid(True)
plt.show()