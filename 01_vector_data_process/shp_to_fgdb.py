#import archook #The module which locates arcgis
#archook.get_arcpy()
import arcpy
import os
arcpy.env.overwriteOutput = True
# -*- coding: utf-8 -*-

# Set environment settings
arcpy.env.workspace = "D:/project_05198/code/201709_SHP2GDB/shapefiles"
outWorkspace = "D:/project_05198/data/04_測試SHP匯入GDB/getSHPs.gdb"

# Execute FeatureClassToFeatureClass
shpList = arcpy.ListFeatureClasses()
for shp in shpList: 
	print shp
	outFeatureClass = shp.strip(".shp")
	arcpy.FeatureClassToFeatureClass_conversion(shp, outWorkspace, outFeatureClass)

print '轉換完成'

