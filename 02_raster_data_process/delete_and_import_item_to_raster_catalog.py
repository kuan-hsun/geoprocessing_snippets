# -*- coding: utf-8 -*-
"""
刪除及新增特定檔案進入指定的raster catalog
"""

#import archook
#archook.get_arcpy()
import arcpy

# set parameters
rasterCatalog = 'D:/project_05198/data/temp/test_topo_dev.gdb/topo_dev'  #指定的raster catalog
changedFile = '3326.tif'  #watchdog監測到的變動檔名

# functions
# 刪除既有raster catalog中的tif
def delItemInCatalog(OID):
    print("deleting item...")
    arcpy.Delete_management(rasterCatalog + '/Raster.OBJECTID =' + OID)
    #arcpy.Delete_management(r'D:\project_05198\data\temp\test_topo_dev.gdb\topo_dev\Raster.OBJECTID = 2')

# 新增tif至raster catalog




with arcpy.da.SearchCursor(rasterCatalog,"*") as cur:
    for row in cur:
        if row[3] == changedFile:   #row[3]of Arc item: name
            print "file changed OID = : " + str(row[0])            #row[0]of Arc item: objectid
            delItemInCatalog(str(row[0]))
            #delItemInCatalog()
        else:
            print "file not found"


