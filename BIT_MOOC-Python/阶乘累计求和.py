#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
描述

获得用户输入的整数n，输出 1!+2!+...+n!的值。

如果输入数值为0、负数、非数字或非整数，
输出提示信息：输入有误，请输入正整数。


输入格式:
使用input()获得系统输入，不增加额外的提示信息。

@author: ZHOU Heng
"""


class Solution:

    def factor(self, n):
        if n in [0, 1]:
            return n
        else:
            fat = 1
            for i in range(1, n+1):
                fat *= i
            return fat


    def factorialSum(self, n):
        """
        :type n: int
        :return: int
        """
        sum = 0
        for i in range(n):
            sum += self.factor(i + 1)
        return sum


def test():
    sol = Solution()
    n = input()
    try:
        n = int(n)
    except:
        print("输入有误，请输入正整数")
    else:
        if n > 0:
            a = sol.factorialSum(n)
            print(a)
        else:
            print("输入有误，请输入正整数")



if __name__ == "__main__":
    test()
