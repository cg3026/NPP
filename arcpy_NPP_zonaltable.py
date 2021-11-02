# -*- coding:utf-8 -*-

import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = r"F:\NPPpython\mouthlydata\mask"

# Set local variables
inZoneData = "citytrans.shp"
zoneField = "市"
inValueRaster = "SVDNB_npp_20181201-20181231_75N060E_vcmcfg_v10_c201902122100_edit_clip_mask.tif"
outTable = "201812maskzonalcity.csv"


# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

print("check")
# Execute ZonalStatisticsAsTable
outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, inValueRaster,
                                 outTable, "DATA", "MEAN")

print("OK")