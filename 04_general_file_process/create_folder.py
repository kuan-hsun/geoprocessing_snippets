import os, sys
import arcpy

# 在程式所在資料夾建立finish資料夾及放相關更新檔的資料夾
# 使用者輸入欲更新線型的縣市

inputcity = raw_input('請輸入欲更新縣市名稱(e.g.新北市)：')
if inputcity == "新北市":
   city =  "03 New Taipei_C"
elif inputcity == "高雄市":
    city =  "07 Kaohsiung_C"
else:
    city = "otherCity" 

path1 = city
path2 = "finish"

os.mkdir(path1)
os.mkdir(path2)


# 找到對應的縣市資料夾，取出應更新圖層放入縣市資料夾
ROOT = os.path.abspath('.') #程式所在資料夾
pROOT = os.path.abspath("..") #程式所在上層資料夾
arcpy.env.workspace = pROOT


'''
# Set local variables
outWorkspace1 = "\finish"
outWorkspace2 = "D:\documents\03NewTaipei"
inWorkspace1 = "\線型"


# 把對應到的shp用CopyFeatures放到資料夾中
for shapefile in enumerate(inWorkspace1):
   if rail.shp in item:
       outFeatureClass = os.path.join(path2, shapefile.strip("rail.shp", "rail_level.shp"))
       arcpy.CopyFeatures_management(shapefile, outFeatureClass)


# Define Projection


for shapefile in fcList:
    print shapefile
    updateList[] = shapefile
    
print updateList

























