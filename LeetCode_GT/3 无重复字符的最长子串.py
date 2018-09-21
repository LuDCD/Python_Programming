#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 无重复字符的最长子串是 "abc"，其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。

@author: ZHOU Heng
"""
class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        res = 0
        if s is None or len(s) == 0:
            return res
        d = {}
        tmp = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            tmp = i - start + 1
            d[s[i]] = i
            res = max(res, tmp)
        return res

    
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        leg = len(s)
        begIndex = 0
        if leg <= 1:
            longStr = leg
        else:
            longStr = 1
            endIndex = begIndex + 1
            while endIndex <= leg - 1:
                print("startIndex:{},endIndex:{}".format(begIndex, endIndex))
                if s[endIndex] not in s[begIndex: endIndex]:
                    endIndex += 1
                else:
                    longStr = max(longStr, endIndex - begIndex)
                    print("longStr:{}".format(longStr))
                    begIndex = endIndex
                    endIndex += 1
                if endIndex == leg:
                    longStr = max(longStr, endIndex - begIndex)
        return longStr

def main():
    sol = Solution()
    # print(sol.lengthOfLongestSubstring("bbbbb"))    # 1
    # print(sol.lengthOfLongestSubstring("pwwkew"))   # 3
    # print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
    # print(sol.lengthOfLongestSubstring("av"))   # 2
    print(sol.lengthOfLongestSubstring("dvdf"))


if __name__ == "__main__":
    main()