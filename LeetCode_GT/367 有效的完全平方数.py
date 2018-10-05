#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
注意：不要使用任何内置的库函数，如  sqrt。

示例 1：
输入： 16
输出： True

示例 2：
输入： 14
输出： False

@author: ZHOU Heng
"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqrtnum = num**0.5
        sqrtnumStr = str(sqrtnum)
        sqrtList = sqrtnumStr.split('.')
        flag = 0
        if sqrtList[-1] == '0':
            flag = 1

        return bool(flag)

def test():
    sol = Solution()
    print( sol.isPerfectSquare(14) )
    print( sol.isPerfectSquare(16) )


if __name__ == "__main__":
    test()