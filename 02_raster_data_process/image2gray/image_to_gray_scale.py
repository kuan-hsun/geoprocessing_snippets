import os
import cv2
'''
imagepath = r'D:\project_05198\code_python\00_TOPO_update_sample\TOPO_update_tiff_file'
outpath = r'D:\project_05198\code_python\00_TOPO_update_sample\TOPO_update_tiff_file\graytiff'
'''

imagepath = r'D:\project_05198\data\temp\0625'
outpath = r'D:\project_05198\data\temp\0625\gray'

# Read image as grayscale
'''
grayscale_img = cv2.imread(r'D:\project_05198\data\temp\4149.tif', cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'D:\project_05198\data\temp\4149_gray.tif', grayscale_img)
'''


allfile = os.listdir(imagepath)
for file in allfile:
    ext = file.split('.')[1]
    if ext == 'tif':
        print("processing: " + file + "...")
        outFile = os.path.join(outpath, file)
        inFile = os.path.join(imagepath, file)
        
        grayscale_img = cv2.imread(inFile, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(outFile, grayscale_img)

        
