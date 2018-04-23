#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:"abccccdd"
输出:7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

@author: ZHOU Heng
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        oddN = 0
        doubleN = 0
        aSet = set( s )
        for k in aSet:
            t = s.count(k)
            if t % 2 == 0:
                doubleN += t
            else:
                doubleN += (t//2)*2
                oddN += 1

        reN = doubleN
        if oddN > 0:
            reN += 1

        return reN





def test():
    # s = "abccccdde"
    s = 'ccc'
    # s = 'cckcc'
    sol = Solution()
    print( sol.longestPalindrome(s) )


if __name__ == "__main__":
    test()



