# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : TextPosition
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : a class for define text position
---------------------------------------
"""

# Basically refer to the CSS's Box Model
# Margin for position
# Align for content

# History:
# 2020/12/8: Create

from PIL import ImageDraw


# TODO missing align and spacing

class TextPosition:
    # x_type must be "l", "m" or "r"
    # y_type must be "t", "m" or "b"
    # align must be "left", "center" or "right"

    x_type = "",
    x_margin = 0,
    y_type = "",
    y_margin = 0,
    content_align = ""

    def __init__(self,
                 x_type=None,
                 x_margin=0,
                 y_type=None,
                 y_margin=0,
                 content_align=None):
        self.set_x_type(x_type)
        self.set_x_margin(x_margin)
        self.set_y_type(y_type)
        self.set_y_margin(y_margin)
        self.set_content_align(content_align)

    def set_x_type(self, new_x_type):
        x_types = ("l", "m", "r")
        if new_x_type is None:
            self.x_type = "l"
        elif new_x_type not in x_types:
            raise ValueError('x_type must be "l", "m" or "r"')
        else:
            self.x_type = new_x_type

    def set_y_type(self, new_y_type):
        x_types = ("t", "m", "b")
        if new_y_type is None:
            self.y_type = "t"
        elif new_y_type not in x_types:
            raise ValueError('y_type must be "t", "m" or "b"')
        else:
            self.y_type = new_y_type

    def set_x_margin(self, new_x_margin):
        if not isinstance(new_x_margin, int):
            raise ValueError("x_margin must be a integer")
        else:
            self.x_margin = new_x_margin

    def set_y_margin(self, new_y_margin):
        if not isinstance(new_y_margin, int):
            raise ValueError("y_margin must be a integer")
        else:
            self.y_margin = new_y_margin

    def set_content_align(self, new_align):
        if new_align is None:
            self.content_align = "left"
        elif new_align not in ("left", "center", "right"):
            raise ValueError('align must be "left", "center" or "right"')
        else:
            self.content_align = new_align

    def position(self, base_img, text_body, text_font):
        x_total, y_total = base_img.size
        output_x, output_y = 0, 0

        # original size
        original_bbox = ImageDraw.Draw(base_img).textbbox((0, 0), text_body, text_font, spacing=4,
                                                          align=self.content_align)
        print("original_bbox=", original_bbox)

        # X axis offset
        if self.x_type == "l":
            target_x = 0 + self.x_margin
            original_x = original_bbox[0]

        elif self.x_type == "r":
            target_x = x_total - self.x_margin
            original_x = original_bbox[2]

        else:  # x_type == "m"
            target_x = int(x_total / 2) + self.x_margin
            original_x = int((original_bbox[2] + original_bbox[0]) / 2)

        output_x = target_x - original_x

        # Y axis offset
        if self.y_type == "t":
            target_y = 0 + self.y_margin
            original_y = original_bbox[1]

        elif self.y_type == "b":
            target_y = y_total - self.y_margin
            original_y = original_bbox[3]

        else:  # y_type == "m"
            target_y = int(y_total / 2) + self.y_margin
            original_y = int((original_bbox[3] + original_bbox[1]) / 2)

        output_y = target_y - original_y

        return output_x, output_y

    def __str__(self):
        attr_str = ",".join("{}={}".format(k, self.__getattribute__(k)) for k in self.__dict__.keys())
        return "Setting for text position is {" + attr_str + "}"


if __name__ == '__main__':
    from PIL import Image, ImageDraw, ImageFont

    text_position = TextPosition("r", 10, "b", 10)
    font_size = 40
    font_name = "font/FreeMono.ttf"


    def test_case(text_position, font_size, font_name):
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
        text_bbox = draw_obj.textbbox(text_xy, text_body, font=text_font,align=text_position.content_align)
        draw_obj.rectangle(text_bbox, fill=(202, 205, 205, 255))
        print("text_bbox:", text_bbox)

        # text
        draw_obj.text(text_xy, text_body, font=text_font, fill=text_color, align=text_position.content_align)

        # baseline
        draw_obj.line([(0, base_img.size[1] / 2), (base_img.size[0], base_img.size[1] / 2)], fill=(100, 100, 100, 255),
                      width=1)
        draw_obj.line([(base_img.size[0] / 2, 0), (base_img.size[0] / 2, base_img.size[1])], fill=(100, 100, 100, 255),
                      width=1)

        # finish
        out = Image.alpha_composite(base_img, text_layer)
        out.show()


    test_case(text_position, font_size, font_name)
