#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
如果可以变为 1，那么这个数就是快乐数。

示例:
输入: 19
输出: true
解释:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

@author: ZHOU Heng
"""

class Solution:
    def numSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        numList = list(str(n))
        numS = 0
        for e in numList:
            numS += eval(e)**2

        return numS

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 9:
            n = self.numSum(n)

        flag = 0
        if n == 1:
            flag = 1

        return bool(flag)


def test():
    sol = Solution()
    print( sol.isHappy(19) )


if __name__ == "__main__":
    test()