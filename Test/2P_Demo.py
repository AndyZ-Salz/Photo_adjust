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

from PIL import Image as pillowImage
from pyexiv2 import Image as exifImage
from PIL import ImageDraw, ImageFont

# 用pillow读取图片,返回pillow图片对象
def load_image(raw_pic_path):
    raw_pic = pillowImage.open(raw_pic_path)
    return raw_pic

# 用pyexiv2读取exif信息，返回字典
def load_exif(raw_pic_path):
    img = exifImage(raw_pic_path)
    raw_exif = img.read_exif()
    img.close() #不调用该方法会导致内存泄漏，但不会锁定文件描述符。
    return raw_exif

# 生成新尺寸图片，无需返回
# this function modifies the Image object in place.
def img_resize(pic_obj,size_limit):
    new_size=(size_limit,size_limit)
    pic_obj.thumbnail(new_size,resample=1) # resample=PIL.Image.LANCZOS



# 在图片上添加文字，返回新的pillow图片对象
# TODO 改逻辑
def img_text_draw(pic_obj,exif):
    # get an image
    base_img = pic_obj.convert("RGBA")

    # make a blank image for the text, initialized to transparent text color
    text_layer = pillowImage.new("RGBA", base_img.size, (255, 255, 255, 0))

    # get a font
    text_font = ImageFont.truetype("Pillow_Example_Draw/FreeMono.ttf", 40)
    # get a drawing context
    draw_obj = ImageDraw.Draw(text_layer)

    # set text color
    text_color = (255   #R
                  , 255 #G
                  , 255 #B
                  , 255)#A


    # 计算位置
    x,y = base_img.size
    print(x) # 宽
    print(y) # 高

    # draw text #TODO 这里只是演示，后面内容全要改
    draw_obj.text((10, 10), "Hello", font=text_font, fill=text_color)
    draw_obj.text((10, 60), "World", font=text_font, fill=text_color)


    # 后处理，与原始图像合并再转回RGB
    out = pillowImage.alpha_composite(base_img, text_layer)
    out_jpg = out.convert('RGB')

    out_jpg.show()



if __name__ == '__main__':
    demo_pic = "Demo_pic.jpg"
    demo_pic2 = "D7000_test.jpg"

    pic_obj =load_image(demo_pic)
    # print(load_exif(demo_pic))
    # print(load_exif(demo_pic2))
    # img_text_draw(load_image(demo_pic),load_exif(demo_pic))

    img_resize(pic_obj,1000) #
    pic_obj.show()