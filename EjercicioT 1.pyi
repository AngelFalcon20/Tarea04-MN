def f(x):
    return x**3 - x - 1

def metodo_biseccion(a, b, tol, max_iteraciones):
    for i in range(1, max_iteraciones + 1):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c, i
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, max_iteraciones
# Definir los parámetros
a = 1
b = 2
tol = 1e-4
max_iteraciones = 100
# LLamamos a la función de método de bisección
raiz, iteraciones = metodo_biseccion(a, b, tol, max_iteraciones)
# Mostrar el resultado
print("Aproximación de la raíz:", raiz)
print("Número de iteraciones:", iteraciones)


