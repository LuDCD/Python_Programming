#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个正整数，检查他是否为交替位二进制数：
换句话说，就是他的二进制数相邻的两个位数永不相等。

示例 1:
输入: 5
输出: True
解释:5的二进制数是: 101

示例 2:
输入: 7
输出: False
解释:7的二进制数是: 111

示例 3:
输入: 11
输出: False
解释:11的二进制数是: 1011

示例 4:
输入: 10
输出: True
解释:10的二进制数是: 1010


@author: ZHOU Heng
"""

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = 1
        s = bin( n )
        for i in range( len(s) - 3 ):
            if s[i+2] == s[i+3]:
                flag = 0
                break

        return bool(flag)

def test():
    sol = Solution()
    n = 10
    print( sol.hasAlternatingBits(n) )


if __name__ == "__main__":
    test()


