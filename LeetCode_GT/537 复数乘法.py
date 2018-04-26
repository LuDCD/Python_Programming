#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个表示复数的字符串。

返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。

示例 1:
输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

示例 2:
输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。

注意:
输入字符串不包含额外的空格。
输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。输出也应当符合这种形式。

@author: ZHOU Heng
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # (a+jb)*(c+jd) = ac - bd + j(ad+bc)
        aList = a.split('+')    # [a, bi]
        bList = b.split('+')    # [c, di]
        aList[0] = eval( aList[0] )
        bList[0] = eval( bList[0] )
        aList[1] = eval( aList[1][:-1] )
        bList[1] = eval( bList[1][:-1] )

        reList = [0, 0]
        reList[0] = aList[0]*bList[0] - aList[1]*bList[1]
        reList[1] = aList[0]*bList[1] + aList[1]*bList[0]

        return str(reList[0]) + '+' + str(reList[1]) + 'i'

def test():
    # a = "1+-1i";     b = "1+-1i"
    a = "1+1i";     b = "1+1i"
    sol = Solution()
    print( sol.complexNumberMultiply(a, b) )


if __name__ == "__main__":
    test()



