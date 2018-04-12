#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 2^(31).

示例:
输入: x = 1, y = 4
输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

@author: ZHOU Heng
"""
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = x ^ y   # x异或y
        bina = bin(a)

        n = 0
        for i in range(2, len(bina) ):
            n = n + eval(bina[i])

        return n


def test():
    x = 1;      y = 4
    s = Solution()
    print( s.hammingDistance(x, y) )

if __name__ == "__main__":
    test()

