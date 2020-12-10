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
# 2020/10/8: Use it for pic demo
# 2020/12/10: import class TextPosition

from PIL import Image as pillowImage
from pyexiv2 import Image as exifImage
from PIL import ImageDraw, ImageFont
import TextPosition


# 用pillow读取图片,返回pillow图片对象
def load_image(raw_pic_path):
    raw_pic = pillowImage.open(raw_pic_path)
    return raw_pic


# 用pyexiv2读取exif信息，返回字典
# read exif by pyexiv2, return a dict
def load_exif(raw_pic_path):
    img = exifImage(raw_pic_path)
    raw_exif = img.read_exif()
    img.close()  # 不调用该方法会导致内存泄漏，但不会锁定文件描述符。
    return raw_exif


# 生成新尺寸图片，无需返回
# this function modifies the Image object in place.
def img_resize(pic_obj, size_limit):
    new_size = (size_limit, size_limit)
    pic_obj.thumbnail(new_size, resample=1)  # resample=PIL.Image.LANCZOS


# 在图片上添加文字，返回新的pillow图片对象
# add text in picture, return a new pillow's image obj
# TODO 改逻辑
def img_text_draw(pic_obj, exif):
    print(exif)
    # set text body
    # TODO 计算需要显示的文字内容
    text_body = "Photo by Andy·Z\n2020-10-05"

    # get an image
    base_img = pic_obj.convert("RGBA")

    # make a blank image for the text, initialized to transparent text color
    text_layer = pillowImage.new("RGBA", base_img.size, (255, 255, 255, 0))

    # get a font
    font_size = 40
    font_name = "font/世界那么大.ttf"
    # font_name = "font/FreeMono.ttf"
    # font_name = "font/AndyZ_InkPen1.ttf"

    text_font = ImageFont.truetype(font_name, font_size)

    # get a drawing context
    draw_obj = ImageDraw.Draw(text_layer)

    # set text color
    text_color = (255  # R
                  , 255  # G
                  , 255  # B
                  , 255)  # A

    # 计算位置
    text_position = TextPosition.TextPosition("r", 30, "b", 30, 5, "right")

    text_xy = text_position.position(base_img, text_body, text_font)

    print(text_xy)

    # draw text
    draw_obj.text(text_xy, text_body, font=text_font, fill=text_color, align="right")

    # 后处理，与原始图像合并再转回RGB
    out = pillowImage.alpha_composite(base_img, text_layer)
    out_jpg = out.convert('RGB')

    out_jpg.show()
    return out_jpg


if __name__ == '__main__':
    demo_pic = "Demo_pic.jpg"
    demo_pic2 = "D7000_test.jpg"

    # pic_obj =load_image(demo_pic)
    # print(load_exif(demo_pic))
    # print(load_exif(demo_pic2))
    # img_text_draw(load_image(demo_pic),load_exif(demo_pic))

    pic_obj = load_image(demo_pic2)
    img_resize(pic_obj, 1050)
    img_exif = load_exif(demo_pic2)
    img_text_draw(pic_obj, exif=img_exif)  # .save("output/text_q95.jpg", format="jpeg", quality=95)
