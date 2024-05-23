# Literal A intervalo [-1.5,2.5]
def f(x):
    return (x + 3) * (x + 1) * x * (x - 1) * (x - 3)

a = -1.5
b = 2.5
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
print(f"La solución es: {solucion}")