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


from PIL import Image, ImageDraw, ImageFont
from PIL import ExifTags


# 缩略图
def thumbnail(input_pic):
    size = (128, 128)
    im = Image.open(input_pic)
    im.thumbnail(size)
    im.save("output/thumbnail.jpg", "JPEG")

    # 保留exif
    im.save("output/thumbnail_exif.jpg", format="jpeg", exif=im.info['exif'])
    print(im.info)


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
    image.save("output/Dark_gray.jpg")


# 打水印
def water_mark():
    image = Image.open("output/Dark_gray.jpg")
    font = ImageFont.truetype("font/FreeMono.ttf", 50)
    draw = ImageDraw.Draw(image)
    draw.text((50, 50), "TEST", fill=(20, 20, 20), font=font, align="right")

    # image.save("output/water_mark.png")
    #
    # # 不同品质对比
    # image.save("output/water_mark_q10.jpg",format="jpeg",quality=10)
    # image.save("output/water_mark_q50.jpg", format="jpeg", quality=50)
    # image.save("output/water_mark_q75_default.jpg", format="jpeg")
    image.save("output/water_mark_q95.jpg", format="jpeg", quality=95)


if __name__ == '__main__':
    # demo_pic = "Demo_pic.jpg"
    # thumbnail(demo_pic)
    # read_exif(demo_pic)
    # create_img()
    water_mark()
