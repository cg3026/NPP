# coding=utf-8
###########################
#          Step1          #
#  @Input:东亚夜间灯光数据   #
#  @InputType:tif         #
#  @Input:中国全境掩模      #
#  @InputType:shp,sbx.etc #
#  @Output:中国夜间灯光数据  #
#  @OutputType:tif        #
###########################

# from osgeo import gdal
import gdal
import os

path = r"E:/GCG_storage/storage_dataset/NPPpython/NPPoriginimg"
filenames = os.listdir(path)
for filename in filenames:
    if filename[-4:] == ".tif":
        input_raster = path + '/' + filename
        # or as an alternative if the input is already a gdal raster object you can use that gdal object
        input_raster = gdal.Open(input_raster)
        input_shape = r"E:\GCG_storage\storage_dataset\NPPpython\city\jiXi.shp"  # or any other format
        output_raster = 'E:/GCG_storage/storage_dataset/NPPpython/test/out/' + filename.split('.')[0] + '_clip.tif'
        # your output raster file

        ds = gdal.Warp(output_raster,
                       input_raster,
                       format='GTiff',
                       cutlineDSName=input_shape,  # or any other file format
                       # cutlineWhere="FIELD = 'whatever'",
                       # optionally you can filter your cutline (shapefile) based on attribute values
                       dstNodata=-9999)  # select the no data value you like
        ds = None  # do other stuff with ds object, it is your cropped dataset. in this case we only close the dataset.
print("OK")

