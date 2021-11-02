# encoding: utf-8
# @Author : GaoCG
# @File : praProduce.py

import os
import arcpy
import numpy as np
import sympy

path = r"E:/GCG_storage/storage_dataset/NPPpython/test/clip4Jixi/"
path_07 = r"E:/GCG_storage/storage_dataset/NPPpython/test/Standard/F162007.tif"


# 求解R2的值
# 输入：参数a, b, c, y均值, 需校正影像，标准影像
def R2(a_y, b_y, c_y, y_m, array, array_std):
    numx_y = np.long(0)
    numy_y = np.long(0)
    for row in range(array.shape[0]):
        for colum in range(array.shape[1]):
            if (array[row][colum] != 0) & (array_std[row][colum] != 0):
                m = a_y * np.long(array[row][colum]) * np.long(array[row][colum]) + b_y * np.long(
                    array[row][colum]) + c_y - np.long(array_std[row][colum])
                numx_y = numx_y + m * m
                n = np.long(array_std[row][colum]) - y_m
                numy_y = numy_y + n * n
    r = 1 - numx_y / numy_y
    return r


def getPara(path, path_07):
    # 存放所有求得的回归参数，格式为:{year} -> {satellite} -> {a, b, c}
    data = {}
    # 定义变量a, b, c
    a = sympy.symbols("a", real=True)
    b = sympy.symbols("b", real=True)
    c = sympy.symbols("c", real=True)

    # 遍历文件夹
    file = os.listdir(path)
    for filename in file:
        if not filename.endswith(".tif"):
            print("break")
        else:
            # 定义方程所需值
            sumx = np.int64(0)
            sumx2 = np.int64(0)
            sumx3 = np.int64(0)
            sumx4 = np.int64(0)
            sumy = np.int64(0)
            sumxy = np.int64(0)
            sumx2y = np.int64(0)
            print(path + filename)
            # 文件打开
            inputRaster = arcpy.Raster(path + filename)
            stdRaster = arcpy.Raster(path_07)
            # 转化为numpy数组
            arr_std = arcpy.RasterToNumPyArray(stdRaster, nodata_to_value=0)
            arr = arcpy.RasterToNumPyArray(inputRaster, nodata_to_value=0)
            print(arr.shape)
            # 统计有效值
            total = 0
            # 循环计算数值
            for row in range(arr.shape[0]):
                for colum in range(arr.shape[1]):
                    if (arr[row][colum] != 0) & (arr_std[row][colum] != 0):
                        total = total + 1
                        sumx = sumx + np.int64(arr[row][colum])
                        sumy = sumy + np.int64(arr_std[row][colum])
                        sumx2 = sumx2 + np.int64(arr[row][colum]) * np.int64(arr[row][colum])
                        sumx3 = sumx3 + np.int64(arr[row][colum]) * np.int64(arr[row][colum]) * np.int64(arr[row][colum])
                        sumx4 = sumx4 + np.int64(arr[row][colum]) * np.int64(arr[row][colum]) * np.int64(
                            arr[row][colum]) * np.int64(arr[row][colum])
                        sumxy = sumxy + np.int64(arr[row][colum]) * np.int64(arr_std[row][colum])
                        sumx2y = sumx2y + np.int64(arr[row][colum]) * np.int64(arr[row][colum]) * np.int64(
                            arr_std[row][colum])
            # 求y均值
            print("该年份DN总值：%d" % sumx)
            ymean = np.long(sumy / total)
            print(ymean)
            # 定义三个方程组
            f1 = (np.long(sumx2y) - np.long(sumx3) * b - np.long(sumx2) * c) / np.long(sumx4) - a
            f2 = (np.long(sumxy) - np.long(sumx) * c - np.long(sumx3) * a) / np.long(sumx2) - b
            f3 = (np.long(sumy) - np.long(sumx2) * a - np.long(sumx) * b) / np.long(total) - c
            # 求解方程组
            result = sympy.solve([f1, f2, f3], [a, b, c])
            # 获得结果
            m1 = result[a]
            m2 = result[b]
            m3 = result[c]
            # 求取当前影像回归的R2
            r2 = R2(sympy.Float(m1, 5), sympy.Float(m2, 5), sympy.Float(m3, 5), ymean, arr, arr_std)
            # 保存回归参数和R2到par
            par = {"a": sympy.Float(m1, 5), "b": sympy.Float(m2, 5), "c": sympy.Float(m3, 5), "R2": r2}
            # 将par链接到某卫星下
            sat = {filename[0:3]: par}
            # 判断当前年份是否已保存数据
            if data.get(filename[3:7]):
                # 组合同年异星数据
                data.get(filename[3:7]).update(sat)
            else:
                # 直接保存
                data[filename[3:7]] = sat
    # 输出全部data数据
    print(data)


getPara(path, path_07)
