# -*- coding: utf-8 -*-
# 若孔蓋種類為0，蓋部寬度在50~300cm，蓋部長度為0，欄位寫入2(合理)
# 若孔蓋種類為1，蓋部寬度在50~300cm，蓋部長度為50~300cm，欄位寫入2(合理)

import arcpy
arcpy.env.workspace = r"D:\project_05198\data\temp\point"


def unitTrans(in_unit):
    # 尺寸單位 0是mm，1是inch，2是cm，3是m
    conver_param = 0
    if in_unit == 0:
        conver_param = 0.1
    elif in_unit == 1:
        conver_param = 2.54
    elif in_unit == 2:
        conver_param = 1
    elif in_unit == 3:
        conver_param = 100
    return conver_param


fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    print "-------------", fc, "-------------"

    with arcpy.da.UpdateCursor(fc, ["孔蓋種", "尺寸單", "蓋部寬", "蓋部長", "判斷"]) as cursor:
        for row in cursor:

            unit_param = unitTrans(row[1])  # 單位轉換乘數
            width = row[2] * unit_param  # 蓋部寬度
            length = row[3] * unit_param  # 蓋部長度

            if (row[0] == 0) and (50 <= width <= 300) and (length == 0):
                row[4] = 2
                cursor.updateRow(row)
            elif (row[0] == 1) and (50 <= width <= 300) and (50 <= length <= 300):
                row[4] = 2
                cursor.updateRow(row)
            elif row[0] != 0 or row[0] != 1:
                row[4] = 1
                cursor.updateRow(row)
            elif row[0] == None:
                row[4] = 0
                cursor.updateRow(row)
            else:
                print "有其他值"

            print row[0], width, length, u"判斷結果---", row[4]


