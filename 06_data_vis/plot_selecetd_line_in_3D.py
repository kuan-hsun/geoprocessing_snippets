import arcpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

def plotWireframe(x,y,z,c):
    ax.plot_wireframe(x,y,z,color=c)


mxd = arcpy.mapping.MapDocument("CURRENT")
arcpy.mapping.ListLayers(mxd)
layers = arcpy.mapping.ListLayers(mxd)
select_layers = [str(i.name) for i in layers if arcpy.Describe(i.name).fidSet]

for fc in select_layers:
    if numOfLayer%3 == 0:
        color = (0.1, 0.2, 0.5)
    elif numOfLayer%2 == 0:
        color = (0.5, 0.8, 0.5)
    else:
        color = (0.6, 0.2, 0.1)

desc = arcpy.Describe(fc)
geometryType = desc.shapeType

if geometryType == 'Polyline':
    for row in arcpy.da.SearchCursor(fc, ["SHAPE@"]):
        for part in row[0]:
            x = []
            y = []
            z = []
            for pnt in part:
                x.append(pnt.X)
                y.append(pnt.Y)
                if pnt.Z == None:
                    z.append(0)
                else:
                    z.append(pnt.Z)
                plotWireframe(x,y,z,color)
else:
    print fc, "is not Polyline"

plt.show()
                
