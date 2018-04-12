#!/usr/bin/python
# -*- coding:utf8 -*-

# import numpy as np
# a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# print( a.shape )
# print(a[[2]].sum())

words = ["abcd", "dcba", "lls", "s", "sssll"]

a = words[0][::-1]
print(a)
print(a == words[1], a+words[0])
dec = 15
b = bin(dec)    # 十进制转二进制
o = oct(dec)    # 转八进制
h = hex(dec)    # 转十六进制
print( "转其他进制结果：", dec, b, o, h )
print( "转进制函数的返回结果类型：", type(b), type(o), type(h) )
print( "转回十进制：", dec, eval(b), eval(o), eval(h))

print( int("0b1111",2), int("0o17",8), int("0xf",16) )
print( int("1111",2), int("17",8), int("f",16) )
