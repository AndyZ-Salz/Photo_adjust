# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 2P_demo_multi
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2021/8/29: Create

import PnP_Demo
import os

def demo_ver(input, output):
    pic_obj = PnP_Demo.load_image(input)
    PnP_Demo.img_resize(pic_obj, 1050)
    img_exif = PnP_Demo.load_exif(input)
    output_pic = output
    final_pic = PnP_Demo.img_sign_text_draw(pic_obj, exif=img_exif)
    final_pic.save(output_pic, format="jpeg", quality=95)
    PnP_Demo.write_exif(output_pic, img_exif)
    # final_pic.show()

if __name__ == '__main__':
    os.chdir("D:\\照片\\210921 中秋\\")
    for file in os.listdir("PS"):
        if os.path.splitext(file)[1] == ".jpg":
            input_pic = os.path.join("PS",file)
            output_pic = os.path.join("Sign",file)
            demo_ver(input_pic,output_pic)


