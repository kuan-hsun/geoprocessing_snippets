# -*- coding: utf-8 -*-

import arcpy

inShapefile = r"D:\project_05198\data\temp\point\電信人手孔 - 複製.shp"
checkField = r"人手孔編號"
updateField = "check"

with arcpy.da.SearchCursor(inShapefile, [checkField]) as rows:
    # 原始寫法
    #values = [r[0] for r in rows]

    # 過濾空值
    values = []
    for r in rows:
        if r[0] != '':
            values.append(r[0])

#print values[6500:6510]




d = {}
for item in set(values):
    if values.count(item) > 1:
        d[item] = 'Y'
    else:
        d[item] = 'N'

with arcpy.da.UpdateCursor(inShapefile, [checkField, updateField]) as rows:
    for row in rows:
        if row[0] in d:
            row[1] = d[row[0]]
            rows.updateRow(row)

