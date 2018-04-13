#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
请编写一个函数，其功能是将输入的字符串反转过来。

示例：
输入：s = "hello"
返回："olleh"

@author: ZHOU Heng
"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

def test():
    sol = Solution()
    s = "hello"
    print( sol.reverseString( s ))


if __name__ == "__main__":
    test()
