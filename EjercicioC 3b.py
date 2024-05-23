
import numpy as np

def f(x):
    return x - np.tan(x)

a = 0
b = 1.4
tol = 1e-5 #Tolerancia de error

while (b - a) / 2 > tol:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

solucion = (a + b) / 2
print(f"La solución es:{solucion:.6}")