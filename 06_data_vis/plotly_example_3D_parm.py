import arcpy
import plotly
import plotly.plotly as py
from plotly.graph_objs import *


mxd = arcpy.mapping.MapDocument("current")
arcpy.mapping.ListLayers(mxd)
layers = arcpy.mapping.ListLayers(mxd)
select_layers = [str(i.name) for i in layers if arcpy.Describe(i.name).fidSet]


for fc in select_layers:
    desc = arcpy.Describe(fc)
    geometryType = desc.shapeType
    
    if geometryType == 'Polyline':
        for row in arcpy.da.SearchCursor(fc, ["SHAPE@"]):
            for part in row[0]:
                global x,y,z
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
                    #plotWireframe(x,y,z,color)
    else:
        print fc, "is not Polyline"


z1 = x
z2 = y
z3 = z

'''
plotly.offline.plot([
    dict(z=z1, type='surface'),
    dict(z=z2, showscale=False, opacity=0.9, type='surface'),
    dict(z=z3, showscale=False, opacity=0.9, type='surface')], filename = r'D:\khcho_documents\dev_python_code\00_basic function code\plotly_figures\figure.html')
'''



