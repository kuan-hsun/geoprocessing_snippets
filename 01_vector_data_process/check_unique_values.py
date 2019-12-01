# -*- coding: utf-8 -*-
# Script to get unique value in specific field for shp / feature class.

import arcpy

def unique_values(table , field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({row[0] for row in cursor})

data_field = unique_values('your_feature_class_path', 'field_name')

for value in data_field:
    print value
