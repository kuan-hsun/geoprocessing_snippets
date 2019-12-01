import zipfile
import sys
import os
from os.path import dirname, abspath, join

DATA_DIR = dirname(__file__)
file_data = []
for filename in os.listdir(DATA_DIR):
    ext = filename.split('.')[1]
    if ext == 'zip':
        print filename
        with zipfile.ZipFile(filename, 'r') as myzip:
            myzip.extract('_alllayers')

