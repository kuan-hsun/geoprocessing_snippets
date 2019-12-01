#對MXD裡所有圖層投影
import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
arcpy.mapping.ListLayers(mxd)
layers = arcpy.mapping.ListLayers(mxd)

sr = arcpy.SpatialReference("TWD 1997 TM Taiwan")
for fc in layers:
	arcpy.DefineProjection_management(fc,sr)
	
	
