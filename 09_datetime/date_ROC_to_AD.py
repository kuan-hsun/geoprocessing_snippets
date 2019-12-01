# -*- coding: cp950 -*-
'''
日期-民國轉西元
"103/2/10" to "2014/2/10"
'''

def date_ROC_to_AD(date):
    try:
        year_ROC = date.split("/")[0]
        if len(year_ROC) == 3:
            year_AD = int(year_ROC) + 1911
            date_AD = str(year_AD) + "/" + date.split("/")[1] + "/" + date.split("/")[2]
            return date_AD
        else:
            return date
    except  ValueError: #input可能有NULL
        print "input cloumn contains Value Error"

date1 = "103/2/10"
print date_ROC_to_AD(date1)


