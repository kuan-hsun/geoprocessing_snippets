raster = arcpy.sa.Raster('your_raster_file')
thisExtent = raster.extent
xmax = thisExtent.XMax 
ymax = thisExtent.YMax
xmin = thisExtent.XMin
ymin = thisExtent.YMin
fc = 'your_raster_file_extent'
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array1 = arcpy.Array([arcpy.Point(xmin, ymax),arcpy.Point(xmax, ymax),arcpy.Point(xmax, ymin),arcpy.Point(xmin, ymin),arcpy.Point(xmin, ymax)])
polygon1 = arcpy.Polygon(array1)
cursor.insertRow([polygon1])
del cursor
