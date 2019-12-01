

import time
startTime = time.clock()
fc_point = "D:/project_05198/data/temp/ExcavationPoint.shp"
fc_polygon = "D:/project_05198/data/temp/testPolygon.shp"
cursor = arcpy.da.InsertCursor(fc_polygon, ["SHAPE@"])

counter = 0  
coords = []
for row in arcpy.da.SearchCursor(fc_point, ["EID", "SHAPE@X", "SHAPE@Y"]):
	n  = row[0]
	if counter > 0:
		if n == old_n:
			pointObj = arcpy.Point(row[1],row[2])		
			coords.append(pointObj)
		if n != old_n:
			polygonArray = arcpy.Array(coords)
			polygon = arcpy.Polygon(polygonArray)
			cursor.insertRow([polygon])
			
			print(polygon)
			coords = []
	old_n = n
	counter = counter + 1
	print("第" + str(counter) + "筆")

del cursor
print time.clock() - startTime, "seconds"
