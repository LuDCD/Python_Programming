#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个整数 (32位有符整数型)，请写出一个函数来检验它是否是4的幂。

示例:
当 num = 16 时 ，返回 true 。 当 num = 5时，返回 false。

问题进阶：你能不使用循环/递归来解决这个问题吗？

@author: ZHOU Heng
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        flag = 0
        while num >= 4:
            if num % 4 == 0:
                num /= 4
            else:
                break

        if num == 1:
            flag = 1

        return bool(flag)



def test():
    # num = 16
    # num = 32
    # num = 5
    num = 1
    sol = Solution()
    print( sol.isPowerOfFour(num) )


if __name__ == "__main__":
    test()



