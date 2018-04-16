#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例:
输入：
s = "abcd"
t = "abcde"
输出：e

解释：
'e' 是那个被添加的字母。

@author: ZHOU Heng
"""

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tlist = list( t )

        for k in s:
            i = tlist.index(k)
            del tlist[i]

        return tlist[0]

def test():
    s = "abcd";     t = "abcde"
    sol = Solution()
    print( sol.findTheDifference(s, t) )


if __name__ == "__main__":
    test()


