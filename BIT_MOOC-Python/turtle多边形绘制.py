#!/usr/bin/env python
# -*- coding:utf8 -*-

import turtle

def writeEdge(l):
    turtle.fd(l)

def turnLeft(angle):
    turtle.left(angle)

turtle.pensize(5)

# 绘制多边形
def polygon(n, l):      # n:多边形边数； l:多边形边长
    writeEdge(l)
    for i in range(n-1):
        turnLeft(360/n)
        writeEdge(l)


polygon(4,100)      # 正方形
polygon(6,100)      # 6边形

turtle.done()