#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。

给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False


示例：
输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14


注意:
输入的数字 n 不会超过 100,000,000. (1e8)

@author: ZHOU Heng
"""

class Solution(object):
    # 判断一个数是否为素数
    def isPrime(self, num ):
        '''
        :type num: int
        :rtype: bool
        '''
        flag = 0
        if num in [2, 3, 5]:
            flag = 1
        else:
            for i in range(2, int( num**0.5+1 ) ):
                flag = 1
                if num % i == 0:
                    flag = 0
                    break

        return bool( flag )     # 简介写法

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        超时！！！！！！
        """
        factorList = []
        if self.isPrime(num) == False:
            for i in range(1, num//2+1):
                if num % i == 0:
                    factorList.append(i)
            # print( factorList )

        flag = 0
        if sum(factorList) == num:
            flag = 1

        return bool(flag)

def test():
    sol = Solution()
    print( sol.checkPerfectNumber(28) )     # True
    print( sol.checkPerfectNumber(1) )      # False
    print( sol.checkPerfectNumber(100) )
    print( sol.checkPerfectNumber(20996011) )


if __name__ == "__main__":
    test()