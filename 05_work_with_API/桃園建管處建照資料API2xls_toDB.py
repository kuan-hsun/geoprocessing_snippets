# 建管
# 2018.08.07
import ast
import pandas as pd
import json
import requests
import pyodbc

#dateStrings=['發照日期=106年02月']

dateStrings=['發照日期=106年01月','發照日期=106年02月','發照日期=106年03月',
            '發照日期=106年04月','發照日期=106年05月','發照日期=106年06月','發照日期=106年07月','發照日期=106年08月',
            '發照日期=106年09月','發照日期=106年10月','發照日期=106年11月','發照日期=106年12月','發照日期=107年01月', 
            '發照日期=107年02月','發照日期=107年03月','發照日期=107年04月','發照日期=107年05月','發照日期=107年06月',
             '發照日期=107年07月','發照日期=107年08月']


data=[]
for idx in range(len(dateStrings)):
    ongoing_flag=True    
    count=0
    while (ongoing_flag):
        try:
            print("Access API...for ",dateStrings[idx])
            startNum=1+count*100
            url="http://building.tycg.gov.tw/opendata/OpenDataSearchUrl.do?d=OPENDATA&c=BUILDLIC&Start="+str(startNum)+"&" + dateStrings[idx]
            r = requests.post(url) 
            if idx==0 and count==0:
                data=r.json()['data']
            else:
                data=data+r.json()['data']
            count=count+1
            if len(r.json()['data']) <100:
                ongoing_flag=False
        except:
            ongoing_flag=False
            print("API access failed")


# 找出 data['門牌'], ['地號'], ['樓層概要'] 為空值者，填補各項value為空字串，避免相關衍生欄位無法產出:
for item in data:
    if item['門牌'] == []:
        item['門牌'] = [{'戶號': '', '行政區': '', '村里鄰': '', '路街段巷弄': '', '號': '', '樓': ''}]
    if item['地號'] == []:
        item['地號'] = [{'行政區': '', '地段': '', '地號母號': '', '地號子號': ''}]
    if item['樓層概要'] == []:
        item['樓層概要'] = [{'樓層別': '', '樓層高度': '', '樓層面積': '', '樓層用途': ''}]

        
# 建立df
df=pd.read_json(json.dumps(data))
try:
    df['first_address'] = df['門牌'].apply(lambda x:x[0])
except:
    df['門牌'] =''
try:
    df['first_id'] = df['_id'].apply(lambda x:x["$oid"])
except:
    df['first_id'] =''
try:
    df['first__landNum'] = df['地號'].apply(lambda x:x[0])
except:
    df['first__landNum'] =''
try:
    df['first__floor'] = df['樓層概要'].apply(lambda x:x[0])
except:
    df['first__floor'] =''
    
# 引號不相容問題,用ast
df = df.astype(str)
try:
    df['full_address'] = df['first_address'].apply(lambda x:ast.literal_eval(x)['行政區']+ast.literal_eval(x)['村里鄰']+ast.literal_eval(x)['路街段巷弄']+ast.literal_eval(x)['號'])
except:
    df['full_address'] =''

print("export to Excel")
writer = pd.ExcelWriter('export.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
df



## 將資料寫入資料表
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=xxx;DATABASE=xxx;UID=xxx;PWD=xxx')
cursor = conn.cursor()


columns = []
for item in df:
    columns.append(item)


# 建立所有要insert的欄位名稱字串
all_col_name = ''
for item in df:
    all_col_name = all_col_name + '[' + item + ']' + ','
all_col_name = all_col_name[:-1] #去掉字尾逗號


# 範例：
# test1 = "[_id],[qtime],[停車空間]"
# values_to_insert = [("({'$oid': '5b7328a4e40a525f2f158228'})", "b", "法定38輛，獎勵0輛，自設42輛")]


k = 0
while k < len(df.index)-1:
    # 先用List將單一筆更新值存起來 (共35個)
    record_insert_value = []
    i = 0
    while i < len(columns): #35種欄位
        record_insert_value.append(df[columns[i]][k])
        i = i + 1
        
    # 再將List轉為Tuple
    insert_tuple = tuple(record_insert_value)
        
    # 最後建立 values_to_insert
    values_to_insert = []
    values_to_insert.append(insert_tuple)
        
    # 建立 parameter_markers
    parameter_markers = ''
    j = 0
    while j < len(columns):
        parameter_markers = parameter_markers + '?' + ','
        j = j + 1
    parameter_markers = '(' + parameter_markers[:-1] + ')'
    #parameter_markers = "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        
    # INSERT資料
    query = "INSERT INTO test_taoyuan_opendata (" + all_col_name + ") VALUES " + ",".join(parameter_markers for _ in values_to_insert)
    flattened_values = [item for sublist in values_to_insert for item in sublist]
    cursor.execute(query, flattened_values)
        
    k = k + 1


conn.commit()

print("table committed")



''' 單筆的情況
# 先用List將單一筆更新值存起來 (共35個)
record_insert_value = []
i = 0
while i < len(columns): #35種欄位
    record_insert_value.append(df[columns[i]][100])   #---100
    i = i + 1

# 再將List轉為Tuple
insert_tuple = tuple(record_insert_value)

# 最後建立 values_to_insert
values_to_insert = []
values_to_insert.append(insert_tuple)

# 建立 parameter_markers
parameter_markers = "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"


query = "INSERT INTO test_taoyuan_opendata (" + all_col_name + ") VALUES " + ",".join(parameter_markers for _ in values_to_insert)
flattened_values = [item for sublist in values_to_insert for item in sublist]
cursor.execute(query, flattened_values)

'''














