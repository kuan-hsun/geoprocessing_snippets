# -*- coding: utf-8 -*-
import arcpy

arcpy.env.workspace = r"your_working_path"
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    inFeatures = fc
    outLocation = r"your_output_path"
    arcpy.arcpy.FeatureClassToFeatureClass_conversion(fc, outLocation, fc)

print "finished"
