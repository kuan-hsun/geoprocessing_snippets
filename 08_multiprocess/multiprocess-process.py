import arcpy
import multiprocessing
import time

'''
process
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

    worker_1 = multiprocessing.Process(target = getDemByNormalLine, args=(whereRange1,))
    worker_2 = multiprocessing.Process(target = getDemByNormalLine, args=(whereRange2,))

    worker_1.start()
    worker_2.start()

    worker_1.join()
    worker_2.join()

    time_end = time.clock()
    print "process: {}".format(str(time_end - time_start))
