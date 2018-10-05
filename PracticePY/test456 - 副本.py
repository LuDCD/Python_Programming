#!/usr/bin/env python
# -*- coding:utf8 -*-

import matplotlib.pyplot as plt
import tensorflow as tf

# 读取图像的原始数据
# name = "./image/DYX.png"
name = "./image/erkang.jpg"
img_raw_data = tf.gfile.FastGFile(name, "rb").read()

# 处理
with tf.Session() as sess:
    # 解码
    img_data = tf.image.decode_jpeg(img_raw_data)
    # img_data = tf.image.decode_png(img_raw_data)  # .png decode
    # 转化为实数型
    img_data = tf.image.convert_image_dtype(img_data, dtype=tf.float32)

    # 调整大小
    # img_resized = tf.image.resize_images(img_data, [300, 300], method=1)


    # 翻转
    img_fliped_lr = tf.image.flip_left_right(img_data)
    img_fliped_ud = tf.image.flip_up_down(img_data)
    # print(img_data.eval())

    # 展示图像
    # plt.imshow(img_data.eval())
    # plt.imshow(img_resized.eval())
    plt.imshow(img_fliped_lr.eval())
    plt.show()
    plt.imshow(img_fliped_ud.eval())
    plt.show()