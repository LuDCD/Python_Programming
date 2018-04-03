#!/usr/bin/env python
# -*- coding:utf8 -*-

import turtle
# 绘图库 turtle

turtle.setup(650, 350, 200, 200)

turtle.penup()      # 抬起画笔，海龟在飞行
turtle.fd(-250)     # 前进 -250 像素

turtle.pendown()    # 落下画笔，海龟在爬行
turtle.pensize(25)

turtle.pencolor("purple")
turtle.seth(-40)

for i in range(8):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)

turtle.circle(40,80/2)
turtle.fd(40)

turtle.circle(16,180)
turtle.fd(40* 2/3)

turtle.done()