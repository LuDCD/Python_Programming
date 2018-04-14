#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3. 如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：
n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

@author: ZHOU Heng
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 输出从 1 到 n 数字的字符串表示。
        # 1. 如果 n 是3的倍数，输出“Fizz”；
        # 2. 如果 n 是5的倍数，输出“Buzz”；
        # 3. 如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
        s = [ 'Fizz', 'Buzz' ]
        reList = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                reList.append( s[0]+s[1] )
            elif i % 3 == 0:
                reList.append( s[0] )
            elif i % 5 == 0:
                reList.append( s[1] )
            else:
                reList.append( str(i) )

        return reList

def test():
    sol = Solution()
    n =15
    print( sol.fizzBuzz(n) )


if __name__ == "__main__":
    test()

