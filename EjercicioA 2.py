import math

# Datos del problema
g = 9.81  # m/s^2
m = 0.25  # kg
k = 0.1   # Ns/m
s0 = 300  # m

# Función para calcular la altura
def altura(t):
    return s0 - (m * g / k) * t + (m ** 2 * g / k ** 2) * (1 - math.exp(-k * t / m))

#Intervalos
t_inicio = 0
t_fin = 100

while (t_fin - t_inicio) > 0.01:
    t_medio = (t_inicio + t_fin) / 2
    altura_a_t_medio = altura(t_medio)

    # Verificación si el objeto ha llegado al piso
    if abs(altura_a_t_medio) < 0.01:
        tiempo_caida = t_medio
        break
    elif altura_a_t_medio > 0:
        # El objeto aún no llega al piso
        t_inicio = t_medio
    else:
        # El objeto ya llego al piso
        t_fin = t_medio
else:
    tiempo_caida = (t_inicio + t_fin) / 2

# Resultado
print(f"El tiempo que tarda en caer es: {tiempo_caida:.2} segundos")