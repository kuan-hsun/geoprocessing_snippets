# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:40:02 2018

@author: khcho
"""

import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=xxx;DATABASE=xxx;UID=xxx;PWD=xxx')
cursor = conn.cursor()

# 建立資料表 --my_test_from_py
#cursor.execute("create table my_test_from_py (varA varchar(100))")
s

# 將資料寫入資料表
mydata = ["data_1", "data_2", "data_3"]

for sw in mydata:
  cursor.execute("""INSERT INTO my_test_from_py VALUES (?)""", sw) # SQL述句的參數透過ODBC, 用?表示

conn.commit()