# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : Simple_Demo
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Function test
---------------------------------------
"""

# History:
# 2020/7/5: Create


from PIL import Image


def thumbnail(input_pic, output_pic):
    size = (128, 128)
    im = Image.open(input_pic)
    im.thumbnail(size)
    im.save(output_pic, "JPEG")


def read_exif(input_pic):
    im = Image.open(input_pic)
    print(im.info)



if __name__ == '__main__':
    demo_pic ="Demo_pic.jpg"
    # thumbnail(demo_pic, "output/thumbnail.jpg")
    read_exif(demo_pic)
