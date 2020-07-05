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


if __name__ == '__main__':
    thumbnail("Demo_pic.jpg", "output/thumbnail.jpg")
