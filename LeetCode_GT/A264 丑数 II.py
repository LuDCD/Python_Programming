#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
编写程序找第 n 个丑数。

丑数就是只包含质因子 2, 3, 5 的正整数。

例如， 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 就是前10个丑数。

注意:
1. 1 一般也被当做丑数
2. n不超过1690

@author: ZHOU Heng
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        factorSet = set()

        while num % 2 == 0:
            factorSet.add(2)
            num /= 2

        while num % 3 == 0:
            factorSet.add(3)
            num /= 3

        while num % 5 == 0:
            factorSet.add(2)
            num /= 5

        flag = 0
        if num == 1:
            flag = 1
        return bool(flag)

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 1
        uglyNum = 1
        while cnt != n:
            uglyNum += 1
            # print( uglyNum )
            # if uglyNum % 7 != 0 and uglyNum % 11 != 0 and uglyNum % 13 != 0:
            if uglyNum % 2 == 0 or uglyNum % 3 == 0 or uglyNum % 5 == 0:
                    if uglyNum % 17 != 0 and self.isUgly(uglyNum):
                        # print( cnt )
                        # print( uglyNum )
                        cnt += 1

        return uglyNum


def test():
    sol = Solution()
    print( sol.nthUglyNumber(1000) )


if __name__ == "__main__":
    test()

'''
超时！！！
'''

