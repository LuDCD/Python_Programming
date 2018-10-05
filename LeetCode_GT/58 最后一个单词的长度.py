#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5

@author: ZHOU Heng
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        leg = 0
        endIndex = -1
        while len(s) > 0 and endIndex >= -len(s) and s[endIndex] != ' ':
            endIndex -= 1
            leg += 1

        return leg

def test():
    s = "Hello World"
    sol = Solution()
    print( sol.lengthOfLastWord(s) )
    print( sol.lengthOfLastWord('wwww ') )
    print( sol.lengthOfLastWord('a') )
    print( sol.lengthOfLastWord('a ') )


if __name__ == "__main__":
    test()



