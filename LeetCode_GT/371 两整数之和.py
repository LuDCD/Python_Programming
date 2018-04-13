#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
不使用运算符 + 和-，计算两整数a 、b之和。

示例：
若 a = 1 ，b = 2，返回 3。

@author: ZHOU Heng
"""

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # return a+b

        return sum( [a,b] )

