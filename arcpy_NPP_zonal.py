# -*- coding:utf-8 -*-

import arcpy
from arcpy import env
from arcpy.sa import *
# Set environment settings
env.workspace = r"F:\NPPpython\mouthlydata\zonal"
# Set local variables
inZoneData = "citytrans.shp"
zoneField = "市"
inValueRaster = "SVDNB_npp_20181201-20181231_75N060E_vcmcfg_v10_c201902122100_edit_clip_mask.tif"
outTable = "201812maskzonal.txt"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")
print("check")
# Execute ZonalStatistics
outZonalStatistics = ZonalStatistics(inZoneData, zoneField, inValueRaster,
                                     "MEAN", "DATA")
# Save the output
outZonalStatistics.save("F:/NPPpython/mouthlydata/zonal")
print("OK")


