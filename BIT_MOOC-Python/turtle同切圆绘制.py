#!/usr/bin/env python
# -*- coding:utf8 -*-

import turtle

turtle.pensize(5)

for i in range(5):
    r = 50 + i*9
    turtle.seth(90)
    turtle.circle(r)
    turtle.circle(-r)

turtle.done()