import os
path = "D:\\khcho_documents\\tool-20171201\\tool\\API_result\\temp"
count = 0
print (path)

for fname in os.listdir(path):
    #new_fname = "R600_" + fname #加字
    new_fname = fname.replace(".csv", "", 1) #取代
    print os.path.join(path, fname)
    os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
    count = count + 1
