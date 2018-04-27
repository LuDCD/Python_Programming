#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给出一个整数，写一个函数来确定这个数是不是3的一个幂。

后续挑战：
你能不使用循环或者递归完成本题吗？

@author: ZHOU Heng
"""

class Solution(object):
    def isPowerOfThree(self, num):
        """
        :type n: int
        :rtype: bool
        """
        flag = 0
        while num >= 3:
            if num % 3 == 0:
                num /= 3
            else:
                break

        if num == 1:
            flag = 1

        return bool(flag)


def test():
    pass


if __name__ == "__main__":
    test()



