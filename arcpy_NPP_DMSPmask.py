# coding=utf-8
###########################
#          Step3          #
#  @Input:编辑后的夜间数据   #
#  @InputType:tif         #
#  @Input:遮罩             #
#  @InputType:tif         #
#  @Output:中国夜间灯光遮罩  #
#  @OutputType:tif        #
###########################
import arcpy

arcpy.CheckOutExtension('Spatial')

from arcpy import env
from arcpy.sa import *

env.workspace = r"E:\GCG_storage\storage_dataset\NPPpython"
inRaster = r"201812chinaclip_edit.tif"
inMaskData = r"2013mask.tif"
# outExtractByMask = ExtractByMask("201812chinaclip_edit.tif", "2013mask.tif")
outExtractByMask = ExtractByMask(inRaster, inMaskData)
outExtractByMask.save(r"E:/GCG_storage/storage_dataset/NPPpython/test/out/2013mask_mask.tif")
print("OK")
