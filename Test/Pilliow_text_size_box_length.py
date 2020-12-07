# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : Pilliow_text_size_box_length
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : to compare ImageDraw.Draw.textsize & ImageDraw.Draw.textlength & ImageDraw.Draw.textbbox
---------------------------------------
"""

# History:
# 2020/10/21: Create
# 2020/12/4: compare text_size and text_bbox

from PIL import Image, ImageDraw, ImageFont


def plus_xy(xy1, xy2):
    return xy1[0] + xy2[0], xy1[1] + xy2[1]


def plus_bbox_offset(bbox, offset):
    return bbox[0] + offset[0], bbox[1] + offset[1], bbox[2] + offset[0], bbox[3] + offset[1]


if __name__ == '__main__':
    # prepare
    # set text body
    text_body = "LINE1:ABQJKP\nline2:abqjkp"

    # get an image
    base_img = Image.new("RGBA", (500, 200), (255, 255, 255, 255))

    # make a blank image for the text, initialized to transparent text color
    text_layer = Image.new("RGBA", base_img.size, (255, 255, 255, 0))

    # get a font
    font_size = 40
    # font_name = "font/世界那么大.ttf"
    font_name = "font/FreeMono.ttf"
    # font_name = "font/AndyZ_InkPen1.ttf"

    text_font = ImageFont.truetype(font_name, font_size)

    # set text color
    text_color = (0  # R
                  , 0  # G
                  , 0  # B
                  , 255)  # A

    # get a drawing context
    draw_obj = ImageDraw.Draw(text_layer)

    # size
    text_size = draw_obj.textsize(text_body, font=text_font)
    print("text_size:", text_size)

    # bbox
    text_bbox = draw_obj.textbbox((0, 0), text_body, font=text_font)
    print("text_bbox:", text_bbox)

    # offset
    text_offset = text_bbox[:2]
    print("text_offset:", text_offset)

    # length # can't measure length of multiline text
    text_length = draw_obj.textlength("LINE1:ABQJKP", font=text_font)
    print("text_length:", text_length)

    # anchor coordinates of the text
    text_xy = (0, 0)

    # visualization master box
    draw_obj.rectangle([(0, 0), (base_img.size[0] - 1, base_img.size[1] - 1)], outline=(25, 25, 25, 255))

    # bbox
    draw_obj.rectangle(plus_bbox_offset(text_bbox, text_xy), fill=(202, 205, 205, 255))

    # text
    draw_obj.text(text_xy, text_body, font=text_font, fill=text_color, align="left")

    # size
    draw_obj.rectangle([text_xy, plus_xy(text_size, text_xy)], outline=(0, 255, 0, 255))

    # 后处理，与原始图像合并
    out = Image.alpha_composite(base_img, text_layer)
    out.show()
    out.save("output/text_bbox_q95.jpg", format="jpeg", quality=95)
