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
            t = n % 26
            strRe = alphaList[t] + strRe
            # print( alphaList[t] )
            n = n // 27

        return strRe



def test():
    sol = Solution()
    print( sol.convertToTitle(701) )    # ZY
    print( sol.convertToTitle(25) )     # Y
    print( sol.convertToTitle(28) )     # AB


if __name__ == "__main__":
    test()