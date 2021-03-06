# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : TextPosition
@Version : 1.0
@Author  : Andy Zang
@software: PyCharm
@For     : a class for define text position
---------------------------------------
Due to the textbbox offset problem in the ImageDraw module
This class is used to automatically compensate for the offset and provide a responsive anchor
See: https://github.com/python-pillow/Pillow/issues/5080
"""

# Basically refer to the CSS's Box Model
# Margin for position
# Align for content
# notice: if set type as "m", the margin for x\y will be the offset from center
#       (plus for right\down , minus for left\up)

# History:
# 2020/12/8: Create
# 2021/2/19: add annotate

from PIL import ImageDraw


# TODO missing embedded_color,stroke_fill

class TextPosition:
    # x_type must be "l", "m" or "r"
    # y_type must be "t", "m" or "b"
    # align must be "left", "center" or "right"

    # setting text direction, language or font features is not supported without libraqm
    # direction must be "rtl" (right to left), "ltr" (left to right) or "ttb" (top to bottom).
    # features see OpenType docs
    # language should be a BCP 47 language code.

    x_type = None
    x_margin = 0
    y_type = None
    y_margin = 0
    text_spacing = 4
    text_align = None
    text_direction = None
    text_features = None
    text_language = None
    text_stroke_width = 0

    def __init__(self,
                 x_type=None,
                 x_margin=0,
                 y_type=None,
                 y_margin=0,
                 text_spacing=4,
                 text_align=None,
                 text_direction=None,
                 text_features=None,
                 text_language=None,
                 text_stroke_width=0
                 ):
        self.set_x_type(x_type)
        self.set_x_margin(x_margin)
        self.set_y_type(y_type)
        self.set_y_margin(y_margin)
        self.set_text_spacing(text_spacing)
        self.set_text_align(text_align)
        self.set_text_direction(text_direction)
        self.set_text_features(text_features)
        self.set_text_language(text_language)
        self.set_text_stroke_width(text_stroke_width)

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

    def set_text_spacing(self, text_spacing):
        if not isinstance(text_spacing, int):
            raise ValueError("text_spacing must be a integer")
        else:
            self.text_spacing = text_spacing

    def set_text_align(self, new_align):
        if new_align is None:
            self.text_align = "left"
        elif new_align not in ("left", "center", "right"):
            raise ValueError('align must be "left", "center" or "right"')
        else:
            self.text_align = new_align

    def set_text_direction(self, new_text_direction):
        direction_types = ("ltr", "rtl", "ttb")
        if new_text_direction is None:
            self.text_direction = None
        elif new_text_direction not in direction_types:
            raise ValueError('direction must be "ltr", "rtl" or "ttb"')
        else:
            self.text_direction = new_text_direction

    def set_text_features(self, new_text_features):
        if new_text_features is None:
            self.text_features = None
        else:
            self.text_features = new_text_features

    def set_text_language(self, new_text_language):
        if new_text_language is None:
            self.text_language = None
        else:
            self.text_language = new_text_language

    def set_text_stroke_width(self, new_stroke_width):
        if not isinstance(new_stroke_width, int):
            raise ValueError("stroke_width must be a integer")
        else:
            self.text_stroke_width = new_stroke_width

    def position(self, base_img, text_body, text_font):
        x_total, y_total = base_img.size
        output_x, output_y = 0, 0

        # original size
        original_bbox = ImageDraw.Draw(base_img).textbbox((0, 0), text_body, text_font, spacing=self.text_spacing,
                                                          align=self.text_align, direction=self.text_direction,
                                                          features=self.text_features, language=self.text_language,
                                                          stroke_width=self.text_stroke_width)

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
