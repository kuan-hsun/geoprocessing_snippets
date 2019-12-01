raster = arcpy.sa.Raster('高鐵旗山斷層_ps_S1d_defo_48期_mean_v')
thisExtent = raster.extent
xmax, ymax, xmin, ymin = thisExtent.XMax, thisExtent.YMax, thisExtent.XMin, thisExtent.YMin
fc = '高鐵_旗山斷層_extent'
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array1 = arcpy.Array([arcpy.Point(xmin, ymax),arcpy.Point(xmax, ymax),arcpy.Point(xmax, ymin),arcpy.Point(xmin, ymin),arcpy.Point(xmin, ymax)])
polygon1 = arcpy.Polygon(array1)
cursor.insertRow([polygon1])
del cursor
