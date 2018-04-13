#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
与 Excel表列名称 问题类似。
给定一个Excel表格中的列名称，返回其相应的列序号。

示例:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

@author: ZHOU Heng
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sList = list( s )
        aOrd = ord( 'A' )

        n = 0
        tList = sList
        for i in range( len(sList) ):
            n = n + ( ord(tList.pop()) - aOrd +1 ) * ( 26**i)       # 按位加权

        return n


def test():
    sol = Solution()
    s = "AC"
    print( sol.titleToNumber(s) )


if __name__ == "__main__":
    test()
