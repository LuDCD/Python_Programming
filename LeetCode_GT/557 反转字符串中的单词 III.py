#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

@author: ZHOU Heng
"""

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        sList = s.split(' ')
        reStr = ''
        l = len(sList)
        for k in range( l ):
            reStr = reStr + sList[k][::-1]
            if k != l-1:
                reStr = reStr + ' '

        return reStr




def test():
    s = Solution()
    st = "Let's take LeetCode contest"
    print( s.reverseWords(st))

if __name__ == "__main__":
    test()