#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格 。 整数除法仅保留整数部分。

示例 1:
输入: "3+2*2"
输出: 7

示例 2:
输入: " 3/2 "
输出: 1

示例 3:
输入: " 3+5 / 2 "
输出: 5

说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

@author: ZHOU Heng
"""

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ''
        for i in range( len(s) ):
            e = s[i]
            if e == '/':
                result = result + '//'
            else:
                result = result + e

        return eval( result )


def test():
    sol = Solution()
    print( sol.calculate(" 3+5 / 2 ") )
    print( sol.calculate(" 3/2 ") )


if __name__ == "__main__":
    test()