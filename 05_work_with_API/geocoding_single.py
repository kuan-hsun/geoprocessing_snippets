# -*- coding: utf-8 -*-
import requests
import pandas as pd
import json
df = pd.read_excel('ORG.xlsx',sheet_name='sheet1')


dataset = []
url='your_domain_name/Geocoding' #API uri

for i,rows in df.iterrows():
    print(df.at[i,'address'])
    address=df.at[i,'address']
    if address == address:
        #r = requests.get(url+"?address="+address)
        r = requests.get(url+"?address="+address, headers={'Authorization': 'access_token myToken'})
        df_get=r.json()
        print(df_get)
        x=df_get['x']
        y=df_get['y']
        village=df_get['village']
        town=df_get['town']
        df.at[i,"x"] = x
        df.at[i,"y"] =y
        df.at[i,"village"] = village
        df.at[i,"town"] =town


writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
print('----------')
