#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import string
import random
import base64

from io import BytesIO
from captcha.image import ImageCaptcha


# 验证码字符集
char_set = string.digits + string.ascii_letters

# 随机生成4位验证码
captcha_text = ''.join(random.sample(char_set, 4))

# 创建图片验证码对象
captcha_image = ImageCaptcha()

# 生成默认验证码
image = captcha_image.generate_image(captcha_text)

# 创建定制验证码
# image = captcha_image.create_captcha_image(captcha_text, (127, 0, 255), (74, 191, 239))

# # 存储验证码到本地
# image.save('%s.png' % captcha_text)
#
# 查看验证码
image.show()

# # 创建内存I/O
# output_buffer = BytesIO()
#
# # 存储到内存
# image.save(output_buffer, format='PNG')
#
# # 读取内存数据
# byte_data = output_buffer.getvalue()
#
# # 转为base64
# image_base64 = base64.b64encode(byte_data)
