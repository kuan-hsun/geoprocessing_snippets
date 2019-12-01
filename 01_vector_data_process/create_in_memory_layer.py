# -*- coding: utf-8 -*-
import arcpy

print "Hello ArcGIS"

arcpy.env.workspace = r"D:\project_05198\data\temp"


arcpy.MakeFeatureLayer_management()


fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    inFeatures = fc
    outLocation = r"D:\project_05198\data\temp"
    arcpy.arcpy.FeatureClassToFeatureClass_conversion(fc, outLocation, fc)

print "finished"
