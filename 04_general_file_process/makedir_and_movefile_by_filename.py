# -*- coding: utf-8 -*-
'''
在指定路徑下，找出相同檔名但不同副檔名的檔案，建立對應資料夾並移入
例如有檔案 sp2017nc_94171ne.tfw 和 sp2017nc_94171ne.tif
則建立 sp2017nc_94171ne 資料夾，並將兩個檔案都移入該資料夾
'''

import os
from os import walk
import shutil


path = r'D:\project_07889\CSRSR_SpotImage_2017\VICE-I1803001\SP2017NC_TWD97\zip'

# 取得不重複的檔名
f_set = set()
for (dirpath, dirnames, filenames) in walk(path):
    for files in filenames:
        f_names = files.split('.')[0]
        f_set.add(f_names)

# 依據檔名建立資料夾
for single_filename in f_set:
    newpath = os.path.join(path, str(single_filename))
    if not os.path.exists(newpath):
        os.makedirs(newpath)


# 將檔案移至對應資料夾
d_set = set()
for (dirpath, dirnames, filenames) in walk(path):
    for d_names in dirnames:
        d_set.add(d_names)

    for files in filenames:
        names = files.split('.')[0]

        moveFile = os.path.join(path, str(files))  # 檔案路徑(包含副檔名)
        targetDir = os.path.join(path, str(names))  # 資料夾路徑(等同檔案名稱)

        if names in d_set:
            print "moving...", names
            shutil.move(moveFile, targetDir)
        else:
            print "skip file:", names
