#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为【非空字符串】且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

@author: ZHOU Heng
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        binA = '0b' + a
        binB = '0b' + b
        binSum = eval(binA) + eval(binB)

        return str(bin(binSum))[2:]


def test():
    # a = "11";       b = "1"
    a = "1010";     b = "1011"
    sol = Solution()
    print( sol.addBinary(a, b) )


if __name__ == "__main__":
    test()



