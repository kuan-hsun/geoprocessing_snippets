# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 00:17:40 2019
@author: KHCho
"""


# 定義表頭和分隔關鍵字
haeder = 'STFR, id, ci, mf, mt, cp, mr, cp, s1, s2, sf, st, cp, sr, cp, stfr'
content = 'STFR , id, ci, mf, mt, cp, mr, s1, s2, sf, st, sr, stfr'


if __name__ == '__main__':
    with open("output.txt", "w") as text_file:
        # 寫表頭
        text_file.write(haeder + '\n')
        # 寫內容
        text_file.write(content + '\n')
