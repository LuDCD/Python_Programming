#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

示例1:
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]

注意:
你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。

@author: ZHOU Heng
"""

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        # list1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        # list2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        # list3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        list1 = set( ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'] )
        list2 = set( ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'] )
        list3 = set( ['z', 'x', 'c', 'v', 'b', 'n', 'm'] )

        reList = []
        for k in words:
            w = set( k.lower() )
            if w <= list1 or w <= list2 or w <= list3:
                reList.append(k)

        return reList


def test():
    s = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print( s.findWords(words) )

if __name__ == "__main__":
    test()