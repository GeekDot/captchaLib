#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import string
import random
from PIL import Image, ImageDraw, ImageFont


# 获取随机RGB颜色
def get_random_color():
    count = 3
    color = []

    while count:
        count -= 1
        color.append(random.randint(120, 200))

    return tuple(color)


# 获取随机验证码
def get_captcha_text():
    return ''.join(random.sample(string.digits + string.ascii_letters, 1))


# 添加验证码文本
def add_captcha_text(draw):

    font = ImageFont.truetype('Medium.ttf', size=36)
    captcha_text = ''

    for i in range(length):
        text = get_captcha_text()
        captcha_text += text
        fill = get_random_color()
        rand_len = random.randint(-5, 5)
        xy = (width * 0.2 * (i + 1) + rand_len, height * 0.2 + rand_len)

        draw.text(xy=xy, text=text, font=font, fill=fill)

    print(captcha_text)


# 添加干扰线
def add_line(draw):

    for i in range(length*3):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        fill = get_random_color()
        xy = (x1, y1, x2, y2)

        draw.line(xy=xy, fill=fill)


# 添加干扰点
def add_point(draw):

    for i in range(length*100):
        fill = get_random_color()
        xy = (random.randint(0, width), random.randint(0, height))

        draw.point(xy=xy, fill=fill)


# 生成验证码
def generate_captcha():

    img = Image.new("RGB", (width, height), (250, 250, 250))
    draw = ImageDraw.Draw(img)

    add_captcha_text(draw)
    add_line(draw)
    add_point(draw)

    # 保存图片
    # img.save(text + ".jpg")
    img.show()


if __name__ == "__main__":
    width = 140
    height = 60
    length = 4
    generate_captcha()
