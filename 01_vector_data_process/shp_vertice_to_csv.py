# 獲取shp所有節點坐標儲存為csv

fc = "D:/arcgisserver/layer/村里_五都版fromSDE/Export_Output_Simp2.shp"
csv = open("D:/arcgisserver/layer/村里_五都版fromSDE/Vertices.csv", "w")
csv.write("X,Y\n")

with arcpy.da.SearchCursor(fc, ("SHAPE@")) as cursor:
    for row in cursor:
        for part in row[0]:
            for pnt in part:
                csv.write("{0},{1}\n".format(pnt.X, pnt.Y))

csv.close()