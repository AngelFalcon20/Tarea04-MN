import math

def f(x):
    return math.sin(math.pi * x)
def biseccion(a, b, tolerancia=1e-6):
    if f(a) * f(b) >= 0:
        print("La función no tiene raíces en el intervalo dado.")
        return None

    while abs(b - a) > tolerancia:
        punto_medio = (a + b) / 2
        if f(punto_medio) == 0:
            return punto_medio
        elif f(a) * f(punto_medio) < 0:
            b = punto_medio
        else:
            a = punto_medio

    return (a + b) / 2
#  a + b = 2
a = 0.5
b = 1.5
solucion = biseccion(a, b)
print(f"La raíz de la función es: {solucion}")
