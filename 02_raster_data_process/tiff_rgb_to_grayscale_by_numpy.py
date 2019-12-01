# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:44:45 2018

@author: 63257

https://stackoverflow.com/questions/7569553/working-with-tiffs-import-export-in-python-using-numpy
"""

from PIL import Image
import numpy as np
import scipy.misc

# 打開檔案
img = r"D:\project_05198\data\12_地形圖_新\測試暗色系\4149.tif"
im = Image.open(img)

# 存為array
imarray = np.array(im)
print(imarray.shape, im.size)


# 更改array內容  -白>黑  其他>灰
for item in imarray:
    for sub_item in item:
        if(np.array_equal(sub_item, np.array([255, 255, 255]))):
            sub_item[0] = 0
            sub_item[1] = 0
            sub_item[2] = 0
        else:
            sub_item[0] = 100
            sub_item[1] = 100
            sub_item[2] = 75

'''
# 更改array內容  -黑>白  白>黑  亮綠>淡綠  亮青藍>暗青藍  亮粉紅>暗粉紅  藍>暗藍
for item in imarray:
    for sub_item in item:
        if(np.array_equal(sub_item, np.array([0, 0, 0]))):
            sub_item[0] = 220
            sub_item[1] = 220
            sub_item[2] = 220
        if(np.array_equal(sub_item, np.array([255, 255, 255]))):
            sub_item[0] = 0
            sub_item[1] = 0
            sub_item[2] = 0
        if(np.array_equal(sub_item, np.array([0, 255, 0]))):
            sub_item[0] = 116
            sub_item[1] = 182
            sub_item[2] = 121   
        if(np.array_equal(sub_item, np.array([0, 255, 255]))):
            sub_item[0] = 100
            sub_item[1] = 175
            sub_item[2] = 175
        if(np.array_equal(sub_item, np.array([255, 0, 255]))):
            sub_item[0] = 161
            sub_item[1] = 125
            sub_item[2] = 161
        if(np.array_equal(sub_item, np.array([0, 0, 255]))):
            sub_item[0] = 115
            sub_item[1] = 115
            sub_item[2] = 155
'''

# 另存檔案
goal_path = r"D:\project_05198\data\12_地形圖_新\測試暗色系\testSave.tif"
scipy.misc.imsave('outfile.tif', imarray)
print('finished')