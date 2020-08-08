# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 2P_Demo
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2020/7/31: Create

from PIL import Image as pillowImage
from pyexiv2 import Image as exifImage


def load_image(raw_pic_path):
    raw_pic = pillowImage.open(raw_pic_path)
    return raw_pic


def load_exif(raw_pic_path):
    raw_exif = exifImage(raw_pic_path).read_exif()
    return raw_exif


if __name__ == '__main__':
    demo_pic = "Demo_pic.jpg"
