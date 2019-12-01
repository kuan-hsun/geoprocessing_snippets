'''
 �b�P�ؿ��U���w�ɦW�A�N�ۦP�ɦW���ɮ����Y��zip
'''

import zipfile
import sys
import os
from os.path import dirname, abspath, join

DATA_DIR = dirname(__file__)

for filename in os.listdir(DATA_DIR):
    ext = filename.split('.')[0]
    print ext
    with zipfile.ZipFile(ext + '.zip', mode = 'w', compression = zipfile.ZIP_DEFLATED) as myzip:
        myzip.write(ext + '.jpg')
        myzip.write(ext + '.jgw')

