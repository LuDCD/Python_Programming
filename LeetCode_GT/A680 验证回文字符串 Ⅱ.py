#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个非空字符串 s，最多删除一个字符。
判断是否能成为回文字符串。

示例 1:
输入: "aba"
输出: True

示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。

注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

@author: ZHOU Heng
"""

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 0    # 标志
        if s == s[::-1]:
            flag = 1
        else:
            for i in range( len(s) ):
                newStr = s[:i] + s[i+1:]
                leg = len( newStr )
                startIndex = 0
                endIndex = leg-1
                while startIndex < endIndex:
                    if newStr[startIndex] != newStr[endIndex]:
                        break
                    startIndex += 1
                    endIndex -= 1
                if startIndex >= endIndex:
                    flag = 1

                # 方法有点慢
                # if newStr == newStr[::-1]:
                #     flag = 1
                #     break

        return bool( flag )


def test():
    sol = Solution()
    print( sol.validPalindrome("aba") )
    print( sol.validPalindrome('a') )
    print( sol.validPalindrome('caba') )
    print( sol.validPalindrome('cba') )
    print( sol.validPalindrome('cbdc') )


if __name__ == "__main__":
    test()
'超时！！'