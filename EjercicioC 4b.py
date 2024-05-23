import numpy as np

def f(x):
    return x - 1 - np.exp(x)

a = -2
b = 0
tol = 1e-5

while (b - a) / 2 > tol:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

solucion = (a + b) / 2
print(f"La solución es:{solucion:.4}")