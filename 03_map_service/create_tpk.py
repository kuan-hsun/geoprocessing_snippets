import arcpy, os

# MXD loop
Workspace = r'D:\Project_Data\05198\temp\test_tif\update2\mxd'
arcpy.env.workspace = Workspace
mxdList = arcpy.ListFiles("*.mxd")
for mapdoc in mxdList:
    filePath = os.path.join(Workspace, mapdoc)
    mxd = arcpy.mapping.MapDocument(filePath)
    basename = os.path.splitext(mapdoc)[0]
    
    # set description
    currentMxd = arcpy.mapping.MapDocument(mxd)
    currentMxd.description = basename
    currentMxd.save()
    
    #Create Map Tile Package
    arcpy.CreateMapTilePackage_management(mxd, "EXISTING", basename +'.tpk', "PNG8", "8",r'D:\Project_Data\05198\temp\test_tif\scheme.xml')





# set description
# ref: https://community.esri.com/thread/108981
mxd = arcpy.mapping.MapDocument(r"C:\temp\python\Airports.mxd")  
mxd.description = "test"
mxd.save()

arcpy.CreateMapTilePackage_management(r'D:\Project_Data\05198\temp\test_tif\update2\UpdateTiles.mxd', "EXISTING", 'Example.tpk', "PNG8", "8",r'D:\Project_Data\05198\temp\test_tif\scheme.xml')