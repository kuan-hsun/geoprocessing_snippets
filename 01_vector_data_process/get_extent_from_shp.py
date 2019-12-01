import arcpy
import os
import threading, time


# Set the workspace
arcpy.env.workspace = "C:/Users/hsun/Desktop/電子地圖更新自動化/02_新北市八里區頂寮五街延伸"
outworkspace = arcpy.env.workspace

# Get a list of all feature classes' extent
fcList = arcpy.ListFeatureClasses() #shp列表

# 抓XY值
fc_extentXMax = [] #對應的範圍list
for fc in fcList:
	desc = arcpy.Describe(fc)
	fc_extentXMax.append(desc.extent.XMax) #依序將範圍加入list

fc_extentYMax = []
for fc in fcList:
	desc = arcpy.Describe(fc)
	fc_extentYMax.append(desc.extent.YMax)

fc_extentXMin = []
for fc in fcList:
	desc = arcpy.Describe(fc)
	fc_extentXMin.append(desc.extent.XMin)

fc_extentYMin = []
for fc in fcList:
	desc = arcpy.Describe(fc)
	fc_extentYMin.append(desc.extent.YMin)

# 找出最大範圍
XMax = max(fc_extentXMax)
XMin = min(fc_extentXMin)
YMax = max(fc_extentYMax)
YMin = min(fc_extentYMin)
print XMax, XMin, YMax, YMin
	

# 將此範圍做成polygon (多20m)
arcpy.CreateFeatureclass_management(outworkspace,'範圍',"POLYGON")
fcextent = "C:/Users/hsun/Desktop/電子地圖更新自動化/02_新北市八里區頂寮五街延伸/範圍.shp"
cursor = arcpy.da.InsertCursor(fcextent, ["SHAPE@"])

# Create an array object needed to create features
array = arcpy.Array([arcpy.Point(XMax+20, YMax+20),
                     arcpy.Point(XMax+20, YMin-20),
					 arcpy.Point(XMin-20, YMin-20),
					 arcpy.Point(XMin-20, YMax+20)])
		
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
		











