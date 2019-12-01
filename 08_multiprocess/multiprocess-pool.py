import arcpy
from multiprocessing import Pool
import time

'''
example for pool.map()
applies the same function to many arguments. 
'''

river_shp = r'D:\temp_data\dem_test\process\HS3_Split7_1_sj.shp'


def getDemByNormalLine(whereRange):
    with arcpy.da.SearchCursor(river_shp, ['FID', 'SHAPE@X', 'SHAPE@Y'], whereRange) as cursor:
        for row in cursor:
            print row[0], row[1], row[2]
            print "----"



if __name__ == '__main__':
    time_start = time.clock()
    
    whereRange1 = '"FID" <= ' + str(500)
    whereRange2 = '"FID" > ' + str(500) + 'and' + '"FID" <= ' + str(1000)
    
    parm_list = [whereRange1, whereRange2]
    pool = Pool(processes=4)
    pool.map(getDemByNormalLine, parm_list)
    pool.close()
    pool.join()


    time_end = time.clock()
    print "Pool: {}".format(str(time_end - time_start))
