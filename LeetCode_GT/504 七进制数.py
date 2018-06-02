#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个【整数】，将其转化为7进制，并以字符串形式输出。

示例 1:
输入: 100
输出: "202"

示例 2:
输入: -7
输出: "-10"

注意: 输入范围是 [-1e7, 1e7] 。

@author: ZHOU Heng
"""

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = 1
        if num < 0:
            flag = 0

        num = abs(num)
        numBase7 = ''
        while num >= 7:
            t = num % 7
            numBase7 = str(t) + numBase7
            num = num // 7

        numBase7 = str(num) + numBase7
        if flag == 0:
            numBase7 = '-' + numBase7

        return numBase7


def test():
    sol = Solution()
    print( sol.convertToBase7(100) )
    print( sol.convertToBase7(-7) )


if __name__ == "__main__":
    test()