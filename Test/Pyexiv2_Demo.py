# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : Pyexiv2_Demo
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2020/7/7: Create

from pyexiv2 import Image

#读exif
def read_exif(input_pic):
    img = Image(input_pic)
    data = img.read_exif()
    print("exif:",data)
    # data2 = img.read_iptc()
    # print("iptc:", data2)
    # data3 = img.read_xmp()
    # print("xmp:", data3)
    # data4 = img.read_raw_xmp()
    # print("raw_xmp:", data4)
    # data5 = img.read_comment()
    # print("comment:",data5)
    # data6 = img.read_icc()
    # print("icc:",data6)
    img.close()
    return data

#写exif
def write_exif(pic_path,exif_data):
    img = Image(pic_path)
    img.clear_exif()   #这里为防止两套数据冲突清空了已有的原exif
    img.modify_exif(exif_data)
    img.close()

# 从原exif中筛选，一些更改，一些用原有的
def new_exif(exif_data):
    exif_modify = ['Exif.Image.Software']
    exif_retain = ['Exif.Image.Make',
                   'Exif.Image.Model',
                   'Exif.Image.Orientation',
                   'Exif.Image.ExifTag',
                   'Exif.Photo.ExposureTime',
                   'Exif.Photo.FNumber',
                   'Exif.Photo.ExposureProgram',
                   'Exif.Photo.ISOSpeedRatings',
                   'Exif.Photo.DateTimeDigitized',
                   'Exif.Photo.BodySerialNumber',
                   'Exif.Photo.LensSpecification',
                   'Exif.Photo.LensModel'
                   ]

    new_exif_data = {}

    # exif_modify
    new_exif_data['Exif.Image.Software'] = "Andy Z's Python Code"

    # exif_retain
    for exif_item in exif_retain:
        new_exif_data[exif_item] = exif_data[exif_item]

    return new_exif_data


if __name__ == '__main__':
    demo_pic = "Demo_pic.jpg"
    exif_data = read_exif(demo_pic)

    new_exif_data = new_exif(exif_data)

    out_pic = "output/Demo_pic_exif.jpg"
    write_exif(out_pic,new_exif_data)
    read_exif(out_pic)


    read_exif("D7000_test.jpg")
