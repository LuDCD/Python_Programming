#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

示例 1:
输入: 1
输出: "A"

示例 2:
输入: 28
输出: "AB"

示例 3:
输入: 701
输出: "ZY"

@author: ZHOU Heng
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alphaList = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        strRe = ''
        while n:
            t = n // 27
            strRe = alphaList[t] + strRe
            n1 = n // 26
            if n1 != 0:
                strRe = alphaList[n1] + strRe

            n = n - 26*n1 - t

        return strRe



def test():
    sol = Solution()
    print( sol.convertToTitle(701) )
    print( sol.convertToTitle(25) )
    print( sol.convertToTitle(28) )


if __name__ == "__main__":
    test()