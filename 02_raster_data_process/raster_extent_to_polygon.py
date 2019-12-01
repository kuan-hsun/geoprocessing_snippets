raster = arcpy.sa.Raster('���K�X�s�_�h_ps_S1d_defo_48��_mean_v')
thisExtent = raster.extent
xmax, ymax, xmin, ymin = thisExtent.XMax, thisExtent.YMax, thisExtent.XMin, thisExtent.YMin
fc = '���K_�X�s�_�h_extent'
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array1 = arcpy.Array([arcpy.Point(xmin, ymax),arcpy.Point(xmax, ymax),arcpy.Point(xmax, ymin),arcpy.Point(xmin, ymin),arcpy.Point(xmin, ymax)])
polygon1 = arcpy.Polygon(array1)
cursor.insertRow([polygon1])
del cursor
