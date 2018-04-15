#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个罗马数字，将其转换成整数。
返回的结果要求在 1 到 3999 的范围内。

I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000

Rules:
* If I comes before V or X, subtract 1      eg: IV = 4 and IX = 9
* If X comes before L or C, subtract 10     eg: XL = 40 and XC = 90
* If C comes before D or M, subtract 100    eg: CD = 400 and CM = 900

示例
输入："DCXXI"
输出：621

@author: ZHOU Heng
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        aDict = { "IV":4, "IX":9,"XL":40, "XC":90, 'CD':400, 'CM':900 }
        bDict = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }

        l = len(s)
        n = 0
        i = 0

        for k in range(l):
            if i < l:
                if s[i:i+2] in list( aDict.keys() ):
                    n += aDict[ s[i:i+2] ]
                    i += 2
                else:
                    n += bDict[ s[i] ]
                    i += 1

        return n


def test():
    sol = Solution()
    # s = "DCXXI"
    s = 'CDIX'
    print( sol.romanToInt(s) )


if __name__ == "__main__":
    test()


