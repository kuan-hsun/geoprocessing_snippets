'''
import archook #The module which locates arcgis
archook.get_arcpy()
'''
import arcpy
import os

filenames = os.listdir(r"D:\project_05198\data\new_tiff_without_tfw")

#�P�_�O�_��TIF��
def is_tif(filename):
    return filename.endswith(".tif")

#���o�Ҧ�TIF���ɦW
tifs = filter(is_tif, filenames)

#�h�����ɦW���J�slist(�n�Q�ᤩtfw��tif)
tiffList = []
for tif in tifs:
    tifNumber = os.path.splitext(tif)[0] #�h�����ɦW
    print(tifNumber)
    tiffList.append(tifNumber)

    
#�bframe.shp�����tiffList�����ݹϴT��
frame = r"D:\project_05198\data\new_tiff_without_tfw\frame_join.shp"
arcpy.MakeFeatureLayer_management(frame,"framelyr")

for tif in tiffList:
    infc = arcpy.SelectLayerByAttribute_management ("framelyr", "NEW_SELECTION", ("'Text' = '" + tif + "'"))
    for row in arcpy.da.SearchCursor(infc, ["SHAPE@XY"]):
        print(row)
'''
�q�ϴT��shp��X�����ϸ��������I����
1/1000�Ϯت��e 800*600
�ҥHtfw����(���W��) = �����I���� x-400 y+300
'''

        
    x, y = row[0]
    print("{}, {}".format(x, y))

    
    
