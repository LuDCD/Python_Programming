#!/usr/bin/env python
# -*- coding:utf8 -*-
import turtle

def writeEdge(l):
    turtle.fd(l)

def turnLeft(angle):
    turtle.left(angle)

'''
x 为叠边形内角度数，即左转角度数；
n 为叠边形的边数书
有
    (180-x/2) * n = 180 * (n-2)
'''

def dbx(l,angle):
    writeEdge(l)
    n = int(-1+720/angle)
    for i in range(n):
        turnLeft(angle)
        writeEdge(l)

turtle.pensize(5)

# 好像只能画叠边形内角为80度的图
dbx(180,80)
turtle.done()