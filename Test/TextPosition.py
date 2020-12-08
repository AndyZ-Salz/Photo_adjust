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


class TextPosition:
    # x_type must be "l", "m" or "r"
    # y_type must be "t", "m" or "b"
    # align must be "left", "center" or "right"

    x_type = None,
    x_margin = 0,
    y_type = None,
    y_margin = 0,
    content_align = None

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

    def __str__(self):
        attr_str = ",".join("{}={}".format(k, self.__getattribute__(k)) for k in self.__dict__.keys())
        return "Setting for position is {" + attr_str + "}"


if __name__ == '__main__':
    xy = TextPosition("l",10,"b",content_align="center")
    print(xy)
