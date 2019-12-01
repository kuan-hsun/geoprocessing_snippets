# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 00:17:40 2019
@author: KHCho
"""

file = r"D:\khcho_documents\dev_python_code\00_basic function code\txt2table\print.txt"

# 定義表頭和分隔關鍵字
haeder = 'STFR, id, ci, mf, mt, cp, mr, cp, s1, s2, sf, st, cp, sr, cp, stfr'
seprators = ('STFR ', 'id ', 'ci ', 'mf ', 'mt ', 'cp ', 'mr ', 's1 ', 's2 ', 'sf ', 'st ', 'sr ', 'stfr')

# 字串分割
def split(txt, seps):
    default_sep = seps[0]
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]


if __name__ == '__main__':
    with open(file) as f:
        with open("output.csv", "w") as text_file:
            # 寫表頭
            text_file.write(haeder + '\n')
            # 寫內容
            for line in f:
                lineList = split(line, seprators)
                print(lineList)
                lineList.pop(0)  #拿出第一個多餘的分隔區塊
                lineList_fill = ['0' if x=='' else x for x in lineList] #空的補0
                str1 = ','.join(lineList_fill)
                text_file.write(str1 + '\n')
            
    



        
        
