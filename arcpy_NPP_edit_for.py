# coding=utf-8

import gdal
import numpy as np
import os

path = "F:/NPPpython/test/out"
filenames = os.listdir(path)


def save_tif(y, save_dir, geotrans, proj):
    file_driver = gdal.GetDriverByName('Gtiff')
    width = int(y.shape[0])
    height = int(y.shape[1])
    outbandsize = int(y.shape[2])
    output_dataset = file_driver.Create(save_dir, height, width, outbandsize, gdal.GDT_Float32)
    output_dataset.SetProjection(proj)
    output_dataset.SetGeoTransform(geotrans)
    for m in range(outbandsize):
        # 写入数据
        output_dataset.GetRasterBand(m + 1).WriteArray(y[:, :, m])
        # output_dataset.BuildOverviews('average', [2, 4, 8, 16, 32])


# filename_uvvis = r'F:\NPPpython\output\201812chinaclip.tif'

for filename in filenames:
    if filename[-4:] == ".tif":
        input_raster = path + '/' + filename
        img_uvvis = gdal.Open(input_raster)
        W = img_uvvis.RasterXSize  # 栅格矩阵的列数
        H = img_uvvis.RasterYSize  # 栅格矩阵的行数
        C_uvvis = img_uvvis.RasterCount  # 波段数
        im_geotrans = img_uvvis.GetGeoTransform()  # 获取仿射矩阵信息
        im_proj = img_uvvis.GetProjection()

        sub_con = img_uvvis.ReadAsArray()
        sub_con = np.expand_dims(sub_con, axis=2)
        print(sub_con.shape)
        sub_con[sub_con < 0] = 0
        sub_con[sub_con > 270] = 270

        filename = 'F:/NPPpython/test/out/' + filename.split('.')[0] + '_edit.tif'
        save_tif(sub_con, filename, im_geotrans, im_proj)
