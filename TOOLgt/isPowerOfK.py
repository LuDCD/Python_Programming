#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
判断num,是不是 K 的幂

@author: ZHOU Heng
"""

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


def test():
    # num = 16;   K = 4
    num = 1;    K = 900
    print( isPowerOfK(num, K) )


if __name__ == "__main__":
    test()



