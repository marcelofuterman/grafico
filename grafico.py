import matplotlib.pyplot as plt

# Datos: dos arrays de números
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Crear el gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b', label="Datos de ejemplo")

# Etiquetas y título
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico simple con Matplotlib")
plt.legend()

# Mostrar el gráfico
plt.show()
