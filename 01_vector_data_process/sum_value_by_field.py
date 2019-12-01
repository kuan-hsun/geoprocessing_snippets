# -*- coding: utf-8 -*-

'''
依據[欄位1]屬性相同者，則將其[欄位2]加總起來，放到欄位3
例如資料本身是以里為單位，而[欄位1]都是區，[欄位2]是人口數，則[欄位3]就是同一區的人口數總和
'''


import arcpy

fc = r"D:\project_05198\data\temp\point\Export_Output2.shp"


# 取得某欄位不重複值
def unique_values(table , field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({row[0] for row in cursor})    

# 將各不重複值
d = {}
myValues = unique_values(fc , 'AREA')
for uniq_value in myValues:
    print uniq_value # 目前屬性
    list = []
    for row in arcpy.da.SearchCursor(fc, ["AREA", u"判斷"]):
        if row[0] == uniq_value:
            list.append(row[1])
    print sum(list) # 個別加總值
    d[uniq_value] = sum(list)


# 依據加總結果字典比對欄位[0]來更新欄位[1]
with arcpy.da.UpdateCursor(fc, ["AREA", u"結果"]) as cursor:
    for row in cursor:
        row[1] = d[row[0]]
        cursor.updateRow(row)





