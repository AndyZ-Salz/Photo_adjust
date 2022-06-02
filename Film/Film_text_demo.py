# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : Film_text_demo
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2022/6/1: Create

from PIL import Image as pillowImage
from pyexiv2 import Image as exifImage
from PIL import ImageDraw, ImageFont
import TextPosition
import os


# 用pillow读取图片,返回pillow图片对象
# read image by pillow, return a pillowImage obj
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
def img_sign_text_draw(pic_obj):
    # set text body
    text_body = "Photo by Andy·Z"

    # get an image
    base_img = pic_obj.convert("RGBA")

    # make a blank image for the text, initialized to transparent text color
    text_layer = pillowImage.new("RGBA", base_img.size, (255, 255, 255, 0))

    # get a font
    font_size = 18

    font_name = "世界那么大.ttf"

    text_font = ImageFont.truetype(font_name, font_size)

    # get a drawing context
    draw_obj = ImageDraw.Draw(text_layer)

    # set text color
    text_color = (255  # R
                  , 255  # G
                  , 255  # B
                  , 130)  # A

    # 计算位置
    text_position = TextPosition.TextPosition("l", 3, "t", 3, 4, "left")

    text_xy = text_position.position(base_img, text_body, text_font)

    # draw text
    draw_obj.text(text_xy, text_body, font=text_font, fill=text_color, align="left")

    # 后处理，与原始图像合并再转回RGB
    out = pillowImage.alpha_composite(base_img, text_layer)
    out_jpg = out.convert('RGB')

    return out_jpg


# 在图片上添加文字，返回新的pillow图片对象
# add text in picture, return a new pillow's image obj
def img_bottom_text_draw(pic_obj, exif):
    # get an image
    base_img = pic_obj.convert("RGBA")

    total_size = (base_img.size[0] + 20, base_img.size[1] + 40)

    base_layer = pillowImage.new("RGBA", total_size, (255, 255, 255, 0))

    # 计算位置和大小
    base_img_position = (10, 10)

    # draw logo
    base_layer.paste(base_img, box=base_img_position)

    # make a blank image for the text, initialized to transparent text color
    text_layer = pillowImage.new("RGBA", total_size, (255, 255, 255, 0))

    # get a font
    font_size = 19

    font_name = "NotoSansHans-Light.otf"
    # font_name = "NotoSansHans-Thin-Windows.otf"
    # font_name ="点点像素体-方形.ttf"

    text_font = ImageFont.truetype(font_name, font_size)

    # get a drawing context
    draw_obj = ImageDraw.Draw(text_layer)

    # set text color
    text_color = (0  # R
                  , 0  # G
                  , 0  # B
                  , 255)  # A

    # draw date
    photo_date = exif['Exif.Photo.DateTimeOriginal'].split(" ")[0].replace(":", "-")
    text_position = TextPosition.TextPosition("r", 10, "b", 10, 4, "right")
    text_xy = text_position.position(text_layer, photo_date, text_font)
    draw_obj.text(text_xy, photo_date, font=text_font, fill=text_color, align="right")

    # draw film type
    film = exif["Exif.Photo.UserComment"][14:]
    text_position = TextPosition.TextPosition("m", 0, "b", 10, 4, "center")
    text_xy = text_position.position(text_layer, film, text_font)
    draw_obj.text(text_xy, film, font=text_font, fill=text_color, align="center")

    # draw Camera
    camera = exif["Exif.Image.Model"]
    text_position = TextPosition.TextPosition("l", 10, "b", 10, 4, "right")
    text_xy = text_position.position(text_layer, camera, text_font)
    draw_obj.text(text_xy, camera, font=text_font, fill=text_color, align="right")


    # 后处理，与原始图像合并再转回RGB
    out = pillowImage.alpha_composite(base_layer, text_layer)
    out_jpg = out.convert('RGB')

    return out_jpg


def demo_ver(input, output):
    pic_obj = load_image(input)
    img_resize(pic_obj, 1010)
    img_exif = load_exif(input)
    output_pic = output
    signed_pic = img_sign_text_draw(pic_obj)
    final_pic = img_bottom_text_draw(signed_pic, img_exif)

    final_pic.save(output_pic, format="jpeg", quality=95)

    # final_pic.show()


if __name__ == '__main__':
    # os.chdir(r"D:\照片\220306 上海植物园")
    # for file in os.listdir("Br"):
    #     if os.path.splitext(file)[1] == ".jpeg":
    #         input_pic = os.path.join("Br", file)
    #         output_pic = os.path.join("Sign", file)
    #         demo_ver(input_pic, output_pic)

    demo_ver("Demo_pic.jpg", "final_pic.jpg")
    demo_ver("Demo_pic2.jpg", "final_pic2.jpg")
    demo_ver("Demo_pic3.jpg", "final_pic3.jpg")