# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : Draw_Partial_Opacity_Text
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2020/8/21: Create


from PIL import Image, ImageDraw, ImageFont


def demo():
    # get an image
    base = Image.open("hopper.png").convert("RGBA")

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype("FreeMono.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 128))
    # draw text, full opacity
    d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)

    out.save("marked.png")

    out_jpg = out.convert('RGB')
    out_jpg.save("marked.jpg")


if __name__ == '__main__':
    demo()
