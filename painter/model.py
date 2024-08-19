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
d3.quiver(x, y, z, u, v, w, color="r", label="forceA")

u, v, w = fuerzaB
d3.quiver(x, y, z, u, v, w, color="b", label="forceB")

plt.legend()
plt.show()
