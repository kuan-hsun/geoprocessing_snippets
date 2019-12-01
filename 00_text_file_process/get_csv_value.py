# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------
#  author: khcho@2018
#----------------------------------------------------------------------------------
# get_csv_value.py
# Description: Extracts value by column from a csv
# Requirements: Python 2.7
#----------------------------------------------------------------------------------
import csv

thiscsv = 'path_to_csv'
column_name = 'column_1'

with open(thiscsv, 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # row is a dict
        print row[column_name]
        
        
