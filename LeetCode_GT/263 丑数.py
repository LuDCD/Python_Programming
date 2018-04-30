#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
编写程序判断给定的数是否为丑数。

丑数就是只包含质因子 2, 3, 5 的正整数。
例如， 6, 8 是丑数，
而 14 不是，因为它包含了另外一个质因子 7。

注意：
1 也可以被当做丑数。
输入不会超过32位整数的范围。

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


def test():
    sol = Solution()
    print( sol.isUgly(6) )
    print( sol.isUgly(8) )
    print( sol.isUgly(14) )
    print( sol.isUgly(0) )


if __name__ == "__main__":
    test()



