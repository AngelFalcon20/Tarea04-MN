# Literal A intervalo [0,1] con tolerancia de error 10^{-2}

def f(x):
    return x**3 - 7*x**2 + 14*x - 6

a = 0
b = 1
tol = 1e-2 #Tolerancia de error

while (b - a) / 2 > tol:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

solucion = (a + b) / 2
print(f"La solución es: {solucion:.3}")







