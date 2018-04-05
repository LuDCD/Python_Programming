#!/usr/bin/python
# -*- coding:utf8 -*-


# def fact(x): # 求阶乘 factorial.py
#     factorial = 1
#     for i in range(x): # [0,x)
#         factorial = factorial*(i+1)
#     return factorial  # 我是注释
#
# n = int( input('请输入一个数：'))
# print( '%d的阶乘为%d.' % (n, fact(n)) )

print(round(0.1+0.2,1) == 0.3)
print(4**0.5)


lis2= [i for i in range(5)]
print(lis2)

#
# n = int( input() )
# upYear = (1 + n*0.001)**365
# dwYear= (1 - n*0.001)**365
# print("{:.2f},{:.2f},{:d}".format( upYear,dwYear,int( upYear/dwYear) ) )


s='PYTHON'
print("{0:3}".format(s))

name="Python语言程序设计课程"
print(name[0],name[2:-2],name[-1])
