#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。
给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：
输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

注意：
每个输入参数的边界满足 1 <= left <= right <= 10000。

@author: ZHOU Heng
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        reList = []
        for i in range(left, right+1):
            if self.judge(i) == 1:
                reList.append(i)

        return reList

    def judge(self, n):
        strN = str(n)
        flag = 1

        for k in strN:
            t = eval(k)
            if t == 0 or n % t != 0:
                flag = 0

        return flag


def test():
    s = Solution()
    # print( s.judge(13) )
    left = 1;   right = 22
    print( s.selfDividingNumbers(left, right) )

if __name__ == "__main__":
    test()