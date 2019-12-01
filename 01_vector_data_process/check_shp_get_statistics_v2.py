# -*- coding: utf-8 -*-
import arcpy
import csv
import collections

arcpy.env.workspace = r"D:\project_05198\data\temp\point"


def GetPercentage(num, den):
    return "%.2f%%" % (float(num)/float(den)*100)


fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    col_cnt1 = collections.Counter(row[0] for row in arcpy.da.SearchCursor(fc, ["判斷"]))
    col_cnt2 = collections.Counter(row[0] for row in arcpy.da.SearchCursor(fc, ["判斷2"]))
    col_cnt3 = collections.Counter(row[0] for row in arcpy.da.SearchCursor(fc, ["判斷3"]))

total_count_1 = sum(col_cnt1[i] for i in col_cnt1)
total_count_2 = sum(col_cnt2[i] for i in col_cnt2)
total_count_3 = sum(col_cnt3[i] for i in col_cnt3)

searchValues = [0, 1, 2]
for i in searchValues:
    col_cnt1[i] = GetPercentage(col_cnt1[i], total_count_1)
    col_cnt2[i] = GetPercentage(col_cnt2[i], total_count_2)
    col_cnt3[i] = GetPercentage(col_cnt3[i], total_count_3)

# write csv
with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["", "缺少率", "補齊率", "補正率"])
    writer.writerow(["判斷", col_cnt1[0], col_cnt1[1], col_cnt1[2]])
    writer.writerow(["判斷2", col_cnt2[0], col_cnt2[1], col_cnt2[2]])
    writer.writerow(["判斷3", col_cnt3[0], col_cnt3[1], col_cnt3[2]])

print col_cnt1
print col_cnt2
print col_cnt3
