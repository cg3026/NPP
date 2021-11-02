# -*- coding: UTF-8 -*-
import arcpy
import os
arcpy.CheckOutExtension('Spatial')

from arcpy import env
from arcpy.sa import *

path = "F:/NPPpython/mouthlydata/clip"
filenames = os.listdir(path)
print(filenames)
for filename in filenames:
    if filename[-4:] == ".tif":
        print(filename)
        inRaster = path + '/' + filename
        #inRaster = r"201812chinaclip.tif"
        print(inRaster)
        inMaskData = r"F:/NPPpython/test/img/2013mask.tif"
        output_raster = r'F:/NPPpython/mouthlydata/mask/' + filename.split('.')[0] + '_mask.tif'
        print(output_raster)
        outExtractByMask = ExtractByMask(inRaster, inMaskData)
        outExtractByMask.save(output_raster)

print("OK")
