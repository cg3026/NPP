# encoding: utf-8
# @Author : GaoCG
# @File : DNtest.py

import arcpy
import numpy as np
import os

path = "E:/GCG_storage/storage_dataset/city_res/云南省/迪庆藏族自治州/云南省_迪庆藏族自治州_F101993.tif"



#filenames = os.listdir(path)
# for filename in filenames:
total = 0
count = 0
sumx = np.int64(0)
    # if os.path.isdir(path + filename):
    #     continue
    # if not filename.endswith(".tif"):
    #     continue
rr = arcpy.Raster(path)
numpy_rr = arcpy.RasterToNumPyArray(rr, nodata_to_value=-1)
for rows in range(numpy_rr.shape[0]):
    for cols in range(numpy_rr.shape[1]):
        print(numpy_rr[rows][cols])
        if numpy_rr[rows][cols] >= 0:
            if not numpy_rr[rows][cols] == 0:
                count = count + 1
            sumx = sumx + np.int64(numpy_rr[rows][cols])
            total = total + 1
xmean = round(float(sumx) / float(total), 4)
print("当前文件为%s,均值为%f,总值为%d,有值像元数%d,总共像元数%d" % ('云南省_迪庆藏族自治州_F101992.tif', xmean, sumx, count, total))
