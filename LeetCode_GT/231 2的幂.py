#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个整数，写一个函数来判断它是否是2的幂。

@author: ZHOU Heng
"""

class Solution(object):
    def isPowerOfTwo(self, num):
        """
        :type num: int
        :rtype: bool
        """
        flag = 0
        while num >= 2:
            if num % 2 == 0:
                num /= 2
            else:
                break

        if num == 1:
            flag = 1

        return bool(flag)

def test():
    # num = 1
    # num = 16
    # num = 32
    num = 5
    sol = Solution()
    print( sol.isPowerOfFour(num) )


if __name__ == "__main__":
    test()



