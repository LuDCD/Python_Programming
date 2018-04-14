#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给一个非负整数 num，反复添加所有的数字，直到结果只有一个数字。

例如:
设定 num = 38，过程就像： 3 + 8 = 11, 1 + 1 = 2。 由于 2 只有1个数字，所以返回它。

进阶:
你可以不用任何的循环或者递归算法，在 O(1) 的时间内解决这个问题么？

@author: ZHOU Heng
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len( str(num) ) > 1:
            t = [ eval(i) for i in str(num) ]
            num = sum( t )

        return num

        # 题目最快人的解法
        # if not num: return 0
        # return num % 9 or 9


def test():
    sol = Solution()
    num = 138
    print( sol.addDigits(num) )


if __name__ == "__main__":
    test()
