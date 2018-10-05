#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
给定 s = "hello", 返回 "holle".

示例 2：
给定 s = "leetcode", 返回 "leotcede".

注意:
元音字母不包括 "y".

@author: ZHOU Heng
"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel = 'AaEeIiOoUu'
        vowList = []
        for e in s:
            if e in vowel:
                vowList.append(e)
        vowList = vowList[::-1]

        k = 0   # 元音字母的序号
        for i in range(len(s)):
            if s[i] in vowel:
                s[i] = vowList[k]
                k += 1

        return ''.join(s)


def test():
    sol = Solution()
    print( sol.reverseVowels('leetcode') )


if __name__ == "__main__":
    test()