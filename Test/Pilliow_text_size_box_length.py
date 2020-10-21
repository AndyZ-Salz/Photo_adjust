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
from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    # prepare
    # set text body
    text_body = "LINE1:ABQJKP\nline2:abqjkp"

    # get an image
    base_img = Image.new("RGBA", (500, 200), (255, 255, 255, 255))

    # make a blank image for the text, initialized to transparent text color
    text_layer = Image.new("RGBA", base_img.size, (255, 255, 255, 0))

    # get a font
    font_size = 45
    font_name = "font/世界那么大.ttf"
    # font_name = "font/FreeMono.ttf"
    text_font = ImageFont.truetype(font_name, font_size)

    # set text color
    text_color = (0  # R
                  , 0  # G
                  , 0  # B
                  , 255)  # A

    # get a drawing context
    draw_obj = ImageDraw.Draw(text_layer)

    # size
    text_size = draw_obj.textsize(text_body,font=text_font)
    print("text_size:",text_size)

    # bbox
    text_bbox = draw_obj.textbbox((0, 0),text_body,font=text_font)
    print("text_bbox:", text_bbox)

    print(text_font.getbbox("LINE1:ABQJKP"))
    

    # length # can't measure length of multiline text
    text_length = draw_obj.textlength("LINE1:ABQJKP",font=text_font)
    print("text_length:",text_length)

    # visualization
    draw_obj.rectangle([(0,0),(base_img.size[0]-1,base_img.size[1]-1)],outline=(25,25,25,255))

    # bbox
    draw_obj.rectangle(text_bbox, fill=(202, 205, 205, 255))

    # text
    draw_obj.text((0, 0), text_body, font=text_font, fill=text_color, align="left")

    # size
    draw_obj.rectangle([(0, 0), text_size], outline=(0, 255, 0, 255))





    # 后处理，与原始图像合并
    out = Image.alpha_composite(base_img, text_layer)
    out.show()
