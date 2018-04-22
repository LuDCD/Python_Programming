#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
编写一个函数，输入是一个无符号整数，返回的是它所有 位1 的个数（也被称为汉明重量）。
汉明重量是字符串相对于同样长度的零字符串的汉明距离。
从计算方法来讲，一个字符串的汉明重量，就是字符串中非零元素的个数。
对于常用的二进制字符串，就是字符串中数字1的个数。

例如，32位整数 '11' 的二进制表示为 00000000000000000000000000001011，所以函数返回3。

@author: ZHOU Heng
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        nStr = bin(n)
        return  nStr.count('1')

def test():
    n = 12
    sol = Solution()
    print( sol.hammingWeight(n) )



if __name__ == "__main__":
    test()


