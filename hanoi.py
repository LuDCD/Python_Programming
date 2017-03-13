#!/usr/bin/python
# -*- coding:utf8 -*-

def hanoi( n, x, y, z):     # 将 x 上的n个盘子移动到 z 上(借助y)
    if n == 1:
        print( x, ' --> ', z)
    else:
        hanoi( n-1, x, z, y )    # 将 x 上的 n-1 个盘子移动到 y 上
        print( x, ' --> ', z )    # 将 x 底下的最后一个盘子移动到 z 上
        hanoi( n-1, y, x, z )     # 将 y 上的 n-1 个盘子移动到 z 上

hanoi(5,'甲','乙','丙')