#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）

示例 1:
输入: L = 6, R = 10
输出: 4
解释:
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)
示例 2:

输入: L = 10, R = 15
输出: 5
解释:
10 -> 1010 (2 个计算置位, 2 是质数)
11 -> 1011 (3 个计算置位, 3 是质数)
12 -> 1100 (2 个计算置位, 2 是质数)
13 -> 1101 (3 个计算置位, 3 是质数)
14 -> 1110 (3 个计算置位, 3 是质数)
15 -> 1111 (4 个计算置位, 4 不是质数)

注意:
L, R 是 L <= R 且在 [1, 10^6] 中的整数。
R - L 的最大值为 10000。

@author: ZHOU Heng
"""

import math
from ctypes import *

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        numPrime = 0
        for i in range( L, R+1 ):
            s = bin( i )
            nList = [ s[i] for i in range( 2, len(s) )  if s[i] != '0' ]    # 把所有 1 存在列表里
            if self.isPrime( len(nList) ):
                numPrime += 1

        return numPrime

    def isPrime(self, num):
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

        return bool( flag )


def test():
    # L = 10; R = 15
    # L = 6;     R = 10
    L = 665988;     R = 669533
    sol = Solution()
    print( sol.countPrimeSetBits(L, R) )

if __name__ == "__main__":
    test()
'''
测试说，超时了。暂无思路。
https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation/description/
'''
