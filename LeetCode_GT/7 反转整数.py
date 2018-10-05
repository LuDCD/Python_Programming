#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
根据这个假设，如果反转后的整数溢出，则返回 0。

@author: ZHOU Heng
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        symbol = '+'    # 默认为 '+'
        strX = str(x)
        if strX[0] == '-':
            symbol= '-'
            numStr = strX[1:][::-1]
            # print( 'numStr', numStr)
            revX = symbol + numStr
        else:
            revX = symbol + strX[::-1]

        # 删除前导 0,找到第一个不为 0 的数
        leg = len(revX)
        for i in range(1,leg):
            if revX[i] != '0':
                startIndex = i
                break

        revX = symbol + revX[startIndex:]
        # print( revX, type(revX) )

        if (-2)**31 <= eval(revX) <= 2**31 - 1:
            pass
        else:
            revX = '0'

        return eval(revX)


def test():
    sol = Solution()
    # print( sol.reverse(120) )
    print( sol.reverse(-123) )
    print( sol.reverse(123) )
    print( sol.reverse(2147483648) )


if __name__ == "__main__":
    test()