import os, io, json, csv, requests
import time
startTime = time.clock()
'''
範例格式
data = [{
    'a': 1,
    'b': 2,
    'c': 3,
}]   
'''
DATA_DIR = "D:\\project_05198\\data\\10_test_motor\\split_round2\\group\\"

for filename in os.listdir(DATA_DIR):
    print "Loading: %s" % filename

    # 讀取原始資料
    dataset = []

    fRead = open(os.path.join(DATA_DIR, filename), 'r')

    for row in csv.DictReader(fRead):
        data = {
        'SEVEN_AREA': row["SEVEN_AREA"],
        'CENTER_AREA' :row["CENTER_AREA"],
        'SUPPLY_ID': row["SUPPLY_ID"]
        }
        #print(data)
        dataset.append(data)
    #print(dataset)
    fRead.close()

    # 寫入JSON檔案
    with open('data.json', 'w') as f:
        json.dump(dataset, f) #json.dump()回傳物件並須寫入檔案；若用json.dumps()會回傳字串

    # 讀取JSON檔案
    with open('data.json', 'r') as f: 
        inputData = json.load(f)

    # 將JSON檔案內容傳入post request
    url = 'http://ge-lab-211.ceci.com.tw:80/WaterAPI/monitor/geocodingMeterMulti'
    resp = requests.post(url, json = inputData)
    #print(resp.text) # resp.text型別是unicode
    respStr = str(resp.text) # 轉成string

    #將API回傳資料儲存為CSV格式
    respJson = json.loads(respStr)

    with open('D:\\project_05198\\data\\10_test_motor\\API_result\\' + filename + '.csv', 'wb') as f:
        writer = csv.writer(f)

        #write header
        writer.writerow(["hasLocate", "isNum", "SEVEN_AREA", "CENTER_AREA", "num", "SUPPLY_ID", "x", "y"])

        #write content
        for con in respJson:
            writer.writerow([con["hasLocate"], con["isNum"], con["SEVEN_AREA"], con["CENTER_AREA"], con["num"], con["SUPPLY_ID"], con["x"], con["y"]])

    
    
print time.clock() - startTime, "seconds"