#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
判断一个数是否为某些有特殊的数（比如素数等）

@author: ZHOU Heng
"""


# 判断一个数是否为素数
def isPrime(num):
    """
    :type num: int
    :rtype: bool
    """
    flag = 0
    if num in [2, 3, 5]:
        flag = 1
    else:
        for i in range(2, int(num ** 0.5 + 1)):
            flag = 1
            if num % i == 0:
                flag = 0
                break

    return bool(flag)  # 简介写法


# 判断num,是不是 K 的幂
def isPowerOfK(num, K):
    """
    :type n: int
    :rtype: bool
    """
    flag = 0
    while num >= K:
        if num % K == 0:
            num /= K
        else:
            break

    if num == 1:
        flag = 1

    return bool(flag)


if __name__ == "__main__":
    pass
