import numpy as np

# Definimos los datos  que tenemos por defecto
L = 10  # cm
r = 1  # cm
V_objetivo = 12.4  # cm^3
tol = 0.01  # cm

def V(h):
    return L * (0.5 * np.pi * r ** 2 - r ** 2 * np.arcsin(h / r) - h * (r ** 2 - h ** 2) ** 0.5 / 2)


# Intervalo inicial para h
a = 0
b = r

# Método de bisección
while (b - a) / 2 > tol:
    c = (a + b) / 2

    # Calculamos el volumen en el punto medio c
    V_c = V(c)

    if V_c == V_objetivo:
        break
    elif V_c < V_objetivo:
        a = c
    else:
        b = c

h_solucion = (a + b) / 2
print(f"La profundidad del agua es: {h_solucion}")