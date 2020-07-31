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

def read_exif(input_pic):
    img = Image(input_pic)
    data = img.read_exif()
    img.close()
    return data


def write_exif(exif_data):
    img = Image("output/thumbnail.jpg")
    img.modify_exif(exif_data)
    img.close()


if __name__ == '__main__':
    demo_pic = "Demo_pic.jpg"
    exif_data=read_exif(demo_pic)
    write_exif(exif_data)