import os
path = r"D:\project_InSAR\0724\0810_outcsv2\defo_data_tai8_PS_70期\00"
count = 0
print (path)

for fname in os.listdir(path):
    #new_fname = "R600_" + fname #加字
    new_fname = fname.replace("defo_ansi_", "defo_", 1) #取代
    print os.path.join(path, fname)
    os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
    count = count + 1
