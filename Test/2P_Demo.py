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

# 用pillow读取图片
def load_image(raw_pic_path):
    raw_pic = pillowImage.open(raw_pic_path)
    return raw_pic

# 用pyexiv2读取exif信息
def load_exif(raw_pic_path):
    img = exifImage(raw_pic_path)
    raw_exif = img.read_exif()
    img.close() #不调用该方法会导致内存泄漏，但不会锁定文件描述符。
    return raw_exif


if __name__ == '__main__':
    demo_pic = "Demo_pic.jpg"
    demo_pic2 = "D7000_test.jpg"
    print(load_exif(demo_pic))
    print(load_exif(demo_pic2))