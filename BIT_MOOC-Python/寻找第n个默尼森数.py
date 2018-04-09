#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
寻找第n个默尼森数
P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
输入格式:按提示用input()函数输入
输出格式：int类型
输入样例：4
输出样例：127

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

primeList = []
for i in range(100*100):
    if isPrime(i):
        primeList.append(i)

# print(primeList)

def monisen(n):
    moniNum = None

    countN = 0  # 计数，记下是第几个默尼森数

    p = 0
    i = 0
    while True:
        # i += 1;print('i',i)
        m = 2**primeList[p] - 1
        p = p + 1
        # print(m)
        if isPrime(m):
            moniNum = m
            countN += 1
            # print(p)
        if countN == n:
            break

    return  moniNum

print( monisen( int( input() ) ) )