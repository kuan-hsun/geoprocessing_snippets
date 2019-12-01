import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = [302131,302122,302131]
y = [2771222,2771223,2771222]
z = [0,0,0]

x1 = [302133,302128,302131]
y1 = [2771218,2771216,2771222]
z1 = [3,3,3]

ax.plot_wireframe(x,y,z)
ax.plot_wireframe(x1,y1,z1)

plt.show()
