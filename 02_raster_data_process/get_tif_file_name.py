'''
import archook #The module which locates arcgis
archook.get_arcpy()
'''
import arcpy
import os

filenames = os.listdir(r"D:\project_05198\data\new_tiff_without_tfw")

#判斷是否為TIF檔
def is_tif(filename):
    return filename.endswith(".tif")

#取得所有TIF的檔名
tifs = filter(is_tif, filenames)

#去掉副檔名後填入新list(要被賦予tfw的tif)
tiffList = []
for tif in tifs:
    tifNumber = os.path.splitext(tif)[0] #去掉副檔名
    print(tifNumber)
    tiffList.append(tifNumber)

    
#在frame.shp中選取tiffList中所屬圖幅框
frame = r"D:\project_05198\data\new_tiff_without_tfw\frame_join.shp"
arcpy.MakeFeatureLayer_management(frame,"framelyr")

for tif in tiffList:
    infc = arcpy.SelectLayerByAttribute_management ("framelyr", "NEW_SELECTION", ("'Text' = '" + tif + "'"))
    for row in arcpy.da.SearchCursor(infc, ["SHAPE@XY"]):
        print(row)
'''
從圖幅框shp找出對應圖號的中心點坐標
1/1000圖框長寬 800*600
所以tfw坐標(左上角) = 中心點坐標 x-400 y+300
'''

        
    x, y = row[0]
    print("{}, {}".format(x, y))

    
    
