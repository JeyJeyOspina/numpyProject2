import numpy as np
import matplotlib.pyplot as plt


fuerzaA = np.array([1, 0, 0])
fuerzaB = np.array([0, 1, 0])
print("Fuerza A =", fuerzaA)
print("Fuerza B =", fuerzaB)

figura = plt.figure()

d3 = figura.add_subplot(projection="3d")

d3.set_xlim(-1, 1)
d3.set_ylim(-1, 1)
d3.set_zlim(-1, 1)

x, y, z = np.array([0, 0, 0])  # se define el punto de aplicación de la fuerza en el origen

u, v, w = fuerzaA  # breaking the force vector into individual components
d3.quiver(x, y, z, u, v, w, color="r", label="fuerzaA")

u, v, w = fuerzaB
d3.quiver(x, y, z, u, v, w, color="b", label="fuerzaB")

plt.legend()
plt.show()

fuerzaC = fuerzaA + fuerzaB # Numpy permite optimizar las operaciones de arreglos
print("fuerza C =", fuerzaC)

fig = plt.figure()

d3 = fig.add_subplot(projection="3d")

d3.set_xlim(-1, 1)
d3.set_ylim(-1, 1)
d3.set_zlim(-1, 1)

x, y, z = np.array([0, 0, 0])

u, v, w = fuerzaA
d3.quiver(x, y, z, u, v, w, color="r", label="Fuerza A")
u, v, w = fuerzaB
d3.quiver(x, y, z, u, v, w, color="b", label="Fuerza B")
u, v, w = fuerzaC
d3.quiver(x, y , z, u, v, w, color="g", label="Fuerza C")

plt.legend()
plt.show()

