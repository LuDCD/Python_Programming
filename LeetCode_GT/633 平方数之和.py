#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5


示例2:
输入: 3
输出: False

@author: ZHOU Heng
"""

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        flag = 0
        mod = int(c**0.5)
        i = 0
        while i <= mod:
            a = c - i*i
            b = int(a**0.5)
            i += 1
            if a == b*b:
                flag = 1
            if flag == 1:
                break

        return bool(flag)

def main():
    sol = Solution()
    print(sol.judgeSquareSum(0))


if __name__ == "__main__":
    main()