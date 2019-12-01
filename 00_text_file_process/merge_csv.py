# -*- coding: utf-8 -*-
import glob
import pandas as pd
path = 'your_csv_path'

allFiles = glob.glob(path + "/*.csv")

frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
    
frame = pd.concat(list_)

#print(frame)

frame.to_csv('your_csv_path' + '\merge.csv')
