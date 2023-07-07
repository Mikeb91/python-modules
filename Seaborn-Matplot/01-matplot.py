import matplotlib.pyplot as plt
import numpy as np 
# Generamos dos vectores x e y, que nos daran las cordenadas por donde pasará la linea.
x = np.arange(0.0, 2.0, 0.01)

y = 1 + np.sin(2 * np.pi * x)

print(x)

# Generamos dos vectores x e y, que nos daran las cordenadas por donde pasará la linea.
x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)

# Simplemente le pedimos a la librería que dibuje una variable en funcion de la otra
# En el primer lugar va la variable horizontal y en el segundo la vertical
plt.plot(x, y)
#plt.show()

fig = plt.figure()
ax = plt.axes()

 #Se peude obtener el mismo resultado con esta única linea
#fig, ax = plt.subplots()

ax.plot(x, y)
#fig.show()

# Generamos las dos curvas
x = np.arange(-1, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)

x2 = np.arange(0.0, 2.0, 0.01)
y2 = x2

# Generamos la figura y los ejes
fig = plt.figure()
ax = plt.axes()

# Ploteamos las dos lineas
ax.plot(x, y)
ax.plot(x2,y2)
#plt.show()

fig = plt.figure()
ax = plt.axes()
#modificar colores, stilos
ax.plot(x, y, color = 'green', linewidth = 2, linestyle = 'solid')

fig = plt.figure()
ax = plt.axes()

ax.set(xlabel='Tiempo (s)', ylabel='Temperatura (°C)',
       title='Valor de temperatura')

ax.plot(x, y, color = 'grey', linewidth = 2, linestyle = '-')


# Podemos agregarle etiquetas a los ejes y un titulo al gráfico



# Este comando enciende la grilla de referencia 
ax.grid()

# Con este comando pueden guardar la imagen en su pc
#fig.savefig("pepe.png")

plt.show()