class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def GetSide(point, line):
    ax = line.x2 - line.x1
    ay = line.y2 - line.y1
    bx = point.x - line.x1
    by = point.y - line.y1
    judge = ax * by - ay * bx
    
    if judge > 0:
        result = "LEFT"
    elif judge < 0:
        result = "RIGHT"
    else:
        result = "On the line"
    return result
        

if __name__ == '__main__':
    p1 = Point(6, 7)
    p2 = Point(3, 4)
    line1 = line(2, 8, 8, 2)

    print GetSide(p1, line1)
    print GetSide(p2, line1)




#---------------------------------------------------
def GetSide(pt_x, pt_y, line_x1, line_y1, line_x2, line_y2):
    ax = line_x2 - line_x1
    ay = line_y2 - line_y1
    bx = pt_x - line_x1
    by = pt_y - line_y1
    judge = ax * by - ay * bx
    
    if judge > 0:
        result = "LEFT"
    elif judge < 0:
        result = "RIGHT"
    else:
        result = "On the line"
    return result


with arcpy.da.SearchCursor("line_single",['SHAPE@']) as cursor:
    for row in cursor:
        line_x1 = row[0].firstPoint.X
        line_y1 = row[0].firstPoint.Y
        line_x2 = row[0].lastPoint.X
        line_y2 = row[0].lastPoint.Y
    

with arcpy.da.UpdateCursor("point_part",['FID', 'SHAPE@', 'SideOfLine']) as cursor:
    for row in cursor:
        pt_x = row[1].firstPoint.X
        pt_y = row[1].firstPoint.Y
        side = GetSide(pt_x, pt_y, line_x1, line_y1, line_x2, line_y2)
        row[2] = side
        cursor.updateRow(row)


 
# 依據SideOfLine欄位，依照Id順序連接
lineField = "SideOfLine"
sortField = "Id"
arcpy.PointsToLine_management(inFeatures, outFeatures, lineField, sortField)

#---------------------------------------------------------------------------
arcpy.AddField_management(boundary_point, "SideOfLine", "TEXT", 10) #識別點位相對於線段的方向


with arcpy.da.SearchCursor(river_shp_forCalculate,['FID', 'SHAPE@']) as line_cursor:
    for row in line_cursor:
        current_lineID = row[0]
        line_x1 = row[1].firstPoint.X
        line_y1 = row[1].firstPoint.Y
        line_x2 = row[1].lastPoint.X
        line_y2 = row[1].lastPoint.Y
        with arcpy.da.UpdateCursor(boundary_point,['ref_ID', 'SHAPE@', 'SideOfLine']) as pt_cursor:
            for row in pt_cursor:
                if row[0] == current_lineID:
                    pt_x = row[1].firstPoint.X
                    pt_y = row[1].firstPoint.Y
                    side = GetSide(pt_x, pt_y, line_x1, line_y1, line_x2, line_y2)
                    row[2] = side
                    pt_cursor.updateRow(row)
            
arcpy.PointsToLine_management(boundary_point,
                              r'D:\Project_Data\05198\temp\dem_test\boundary_line.shp',
                              "SideOfLine", "ref_ID")

        

        








    

    
    
