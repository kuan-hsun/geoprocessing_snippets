import os, sys
import arcpy

# �b�{���Ҧb��Ƨ��إ�finish��Ƨ��Ω������s�ɪ���Ƨ�
# �ϥΪ̿�J����s�u��������

inputcity = raw_input('�п�J����s�����W��(e.g.�s�_��)�G')
if inputcity == "�s�_��":
   city =  "03 New Taipei_C"
elif inputcity == "������":
    city =  "07 Kaohsiung_C"
else:
    city = "otherCity" 

path1 = city
path2 = "finish"

os.mkdir(path1)
os.mkdir(path2)


# ��������������Ƨ��A���X����s�ϼh��J������Ƨ�
ROOT = os.path.abspath('.') #�{���Ҧb��Ƨ�
pROOT = os.path.abspath("..") #�{���Ҧb�W�h��Ƨ�
arcpy.env.workspace = pROOT


'''
# Set local variables
outWorkspace1 = "\finish"
outWorkspace2 = "D:\documents\03NewTaipei"
inWorkspace1 = "\�u��"


# ������쪺shp��CopyFeatures����Ƨ���
for shapefile in enumerate(inWorkspace1):
   if rail.shp in item:
       outFeatureClass = os.path.join(path2, shapefile.strip("rail.shp", "rail_level.shp"))
       arcpy.CopyFeatures_management(shapefile, outFeatureClass)


# Define Projection


for shapefile in fcList:
    print shapefile
    updateList[] = shapefile
    
print updateList

























