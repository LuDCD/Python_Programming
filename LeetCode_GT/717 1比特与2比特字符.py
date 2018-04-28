#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。
给定的字符串总是由0结束。

示例 1:
输入:
bits = [1, 0, 0]
输出: True
解释:
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。

示例 2:
输入:
bits = [1, 1, 1, 0]
输出: False
解释:
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。

注意:
1 <= len(bits) <= 1000.
bits[i] 总是0 或 1.

@author: ZHOU Heng
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        while len(bits) >= 2:
            if bits[0] == 1:
                del bits[0:2]
            else:
                del bits[0]

        flag = 0

        if bits == [0]:
            flag = 1

        return bool(flag)


def test():
    sol = Solution()
    print( sol.isOneBitCharacter([1, 1, 1, 0]) )
    print( sol.isOneBitCharacter([1, 0, 0]) )
    print( sol.isOneBitCharacter([0,0]) )


if __name__ == "__main__":
    test()



