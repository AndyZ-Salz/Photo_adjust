# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : test_case
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2020/12/10: Create

from PIL import Image, ImageDraw, ImageFont
import TextPosition


def test_case_of_Position(text_position, font_size, font_name):
    # prepare
    # set text body
    text_body = "LINE1:ABQJKP\nline2:abqjkp"

    # get an image
    base_img = Image.new("RGBA", (500, 200), (255, 255, 255, 255))

    # make a blank image for the text, initialized to transparent text color
    text_layer = Image.new("RGBA", base_img.size, (255, 255, 255, 0))

    # get a font

    text_font = ImageFont.truetype(font_name, font_size)

    # set text color
    text_color = (0, 0, 0, 255)

    # get a drawing context
    draw_obj = ImageDraw.Draw(text_layer)

    print(text_position)
    text_xy = text_position.position(base_img, text_body, text_font)

    print("text_xy=", text_xy)

    # visualization master box
    draw_obj.rectangle([(0, 0), (base_img.size[0] - 1, base_img.size[1] - 1)], outline=(25, 25, 25, 255))

    # bbox
    text_bbox = draw_obj.textbbox(text_xy, text_body, font=text_font, align=text_position.text_align,
                                  spacing=text_position.text_spacing, stroke_width=text_position.text_stroke_width)
    draw_obj.rectangle(text_bbox, fill=(202, 205, 205, 255))
    print("text_bbox:", text_bbox)

    # text
    draw_obj.text(text_xy, text_body, font=text_font, fill=text_color, align=text_position.text_align,
                  spacing=text_position.text_spacing, stroke_width=text_position.text_stroke_width)

    # baseline
    draw_obj.line([(0, base_img.size[1] / 2), (base_img.size[0], base_img.size[1] / 2)], fill=(100, 100, 100, 255),
                  width=1)
    draw_obj.line([(base_img.size[0] / 2, 0), (base_img.size[0] / 2, base_img.size[1])], fill=(100, 100, 100, 255),
                  width=1)

    # finish
    out = Image.alpha_composite(base_img, text_layer)
    out.show()


if __name__ == '__main__':
    text_position = TextPosition.TextPosition("m", 0, "m", 0, 4, "center", text_stroke_width=0)
    font_size = 40
    # font_name = "font/FreeMono.ttf"
    font_name = "font/世界那么大.ttf"
    test_case_of_Position(text_position, font_size, font_name)
