# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------
#  author: khcho@2019
#----------------------------------------------------------------------------------
# combine_csv.py
# Description: Merge all the csv in one
# Requirements: Python 2.7
#----------------------------------------------------------------------------------
import glob
import time

csvx_list = glob.glob('*.csv')
time.sleep(2)

for i in csvx_list:
    fr = open(i,'r').read()
    with open('output.csv','a') as f:
        f.write(fr)

time.sleep(10)
