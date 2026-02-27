# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : Pillow_Issue
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2020/12/7: Create


from PIL import Image, ImageDraw, ImageFont

# set text body
text_body = "LINE1:ABQJKP\nline2:abqjkp"

# make a blank image for the text, initialized to transparent text color
text_layer = Image.new("RGBA", (200, 500), (255, 255, 255, 0))

# get a font
font_size = 40
font_name = "font/FreeMono.ttf"
text_font = ImageFont.truetype(font_name, font_size)

# set text color
text_color = (0, 0, 0, 255)

# get a drawing context
draw_obj = ImageDraw.Draw(text_layer)

# bbox
text_bbox = draw_obj.textbbox((0, 0), text_body, font=text_font,anchor="la")
print("text_bbox:", text_bbox)

# text
draw_obj.text((0,0), text_body, font=text_font, fill=text_color,anchor="la")
