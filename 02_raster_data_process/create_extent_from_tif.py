# -*- coding: utf-8 -*-
"""
建立所有異動tif的範圍shp
"""
import os
# import archook
# archook.get_arcpy()
import arcpy
import glob
import arcgisscripting
from arcpy import env
arcpy.env.overwriteOutput = True


def CreateTifExtentShp(path, template, prj):
    # 路徑為存放所有異動tif的資料夾
    env.workspace = path
    env.overwriteOutput = True
    RasterType = 'TIF'
    FileList = glob.glob(path + "\*." + RasterType)
    print 'Reading files from ' + path
    os.chdir(path)
    print FileList
    geometry_type = "POLYGON"
    #template = r"D:\project_05198\data\temp\template.shp"
    has_m = "DISABLED"
    has_z = "DISABLED"

    # Creating a spatial reference object
    spatial_reference = arcpy.SpatialReference(prj)

    x = 0
    z = x+1

    for File in FileList:
        # File=FileList[x]
        RasterFile = arcgisscripting.Raster(File)
        RasterExtent = RasterFile.extent
        print File
        XMAX = RasterExtent.XMax
        XMIN = RasterExtent.XMin
        YMAX = RasterExtent.YMax
        YMIN = RasterExtent.YMin
        pnt1 = arcpy.Point(XMIN, YMIN)
        pnt2 = arcpy.Point(XMIN, YMAX)
        pnt3 = arcpy.Point(XMAX, YMAX)
        pnt4 = arcpy.Point(XMAX, YMIN)
        array = arcpy.Array()
        array.add(pnt1)
        array.add(pnt2)
        array.add(pnt3)
        array.add(pnt4)
        array.add(pnt1)
        polygon = arcpy.Polygon(array)
        arcpy.CreateFeatureclass_management(path, "Temp_Polygon_Extent" + "_" + str(
            z), geometry_type, template, has_m, has_z, spatial_reference)
        arcpy.CopyFeatures_management(
            polygon, "Temp_Polygon_Extent" + "_" + str(z))
        ShapeFile = "Temp_Polygon_Extent" + "_" + str(z) + ".shp"
        print "Created: " + ShapeFile
        arcpy.AddField_management(ShapeFile, 'FileName', 'TEXT')
        desc = arcpy.Describe(ShapeFile)
        print desc, ShapeFile
        #rows = arcpy.InsertCursor(ShapeFile, desc)
        rows = arcpy.UpdateCursor(ShapeFile)
        #row = rows.newRow()
        #row.FileName = str(File)
        #row.FileName = File
        print 'Filled in: ', str(File)
        # rows.insertRow(row)
        for row in rows:
            row.FileName = str(ShapeFile)
            rows.updateRow(row)
        x = x + 1
        z = z + 1

    # cleaning up
    arcpy.CreateFeatureclass_management(
        path, "Extent.shp", geometry_type, template, has_m, has_z, spatial_reference)
    list = []
    lstFCs = arcpy.ListFeatureClasses("Temp_Polygon_Extent*")
    print 'Merging Polygon_Extents* to Extent.shp'

    for fc in lstFCs:
        print fc
        list.append(fc)

    arcpy.Merge_management(list, "Extent_temp.shp")
    #print 'Deleting identical entries and temp files'
    #arcpy.DeleteIdentical_management("Extent.shp", ["SHAPE"])
    arcpy.Dissolve_management("Extent_temp.shp", "Extent.shp")

    sr = arcpy.SpatialReference("TWD 1997 TM Taiwan")
    arcpy.DefineProjection_management("Extent.shp", sr)

    os.makedirs('Extent')
    arcpy.CopyFeatures_management("Extent.shp", 'Extent/Extent.shp')

    arcpy.Delete_management("Extent_temp.shp")
    arcpy.Delete_management("Extent.shp")
    print "------------------------------------------------"
    print 'Created Extent.shp'
    print "------------------------------------------------"
    return "Extent.shp"

    for item in list:
        arcpy.Delete_management(item)
    del row, rows
