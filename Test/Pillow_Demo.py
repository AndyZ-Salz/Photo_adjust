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


from PIL import Image,ImageDraw, ImageFont
from PIL import ExifTags


# 缩略图
def thumbnail(input_pic, output_pic):
    size = (128, 128)
    im = Image.open(input_pic)
    im.thumbnail(size)
    im.save(output_pic, "JPEG")


# 用pillow读取exif
def read_exif(input_pic):
    im = Image.open(input_pic)
    # im_exif = im.info['exif']
    # im_exif = im._getexif()
    # im_exif.decode() # bytes to string

    exif = {
        ExifTags.TAGS[k]: v for k, v in im._getexif().items() if k in ExifTags.TAGS
    }

    print(str(exif))

    exif_ver = exif['ExifVersion']

    print(exif_ver.decode())


# 生成全黑图片
def create_img():
    width = 300
    height = 200
    image = Image.new('RGB', (width, height), (80, 80, 80))
    image.save("output/Dark_gray.jpg", "jpeg")


# 打水印
def water_mark():
    image = Image.open("output/Dark_gray.jpg")
    font = ImageFont.truetype('C:/windows/Fonts/Arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    draw.text((10,10),"TEst")
    image.save("output/water_mark.jpg", "jpeg",align="right")

if __name__ == '__main__':
    # demo_pic = "Demo_pic.jpg"
    # thumbnail(demo_pic, "output/thumbnail.jpg")
    # read_exif(demo_pic)
    water_mark()
