#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
判断一个数是否为素数

@author: ZHOU Heng
"""

import math

def isPrime(num):
    ' 判断一个数是否为素数 '
    flag = 0
    if num in [2, 3, 5]:
        flag = 1
    else:
        for i in range(2, int( math.sqrt(num)+1 ) ):
            flag = 1
            if num % i == 0:
                flag = 0
                break

    if flag == 1:
        return True
    else:
        return False

# print( isPrime(99) )