import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib import cm
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

plt.close(fig)

# plot line
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=10)

ax = fig.add_subplot(1, 2, 2, projection='3d')
X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
plt.show()



import ConversionUtils  
import arcpy   
from arcpy import env   
import matplotlib.pyplot as plt

xLabelName = "x label"  
yLabelName = "y_label"  
title = "Title"  
fig = plt.figure()  
plt.plot(range(10), range(10))  
plt.xlabel(xLabelName, fontsize = 14)   
plt.ylabel(yLabelName, fontsize = 14)   
plt.title(str(title), fontsize = 16)  
plt.grid()   
#plt.savefig("f:/test/abc.png")   
plt.show()  
clf()
