#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转。
如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"

要求:
该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。

@author: ZHOU Heng
"""

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = len(s)
        reStr = ''

        n = l // (2*k)      # n个2k段
        for i in range(n):
            t1 = s[i*2*k : i*2*k+k]
            reStr += t1[::-1]
            reStr += s[i*2*k+k : i*2*k+2*k]

        m = l - n*2*k   # 除n个2k段，剩下m个元素
        if 0 <= m <= k:
            t2 = s[n*2*k : ]
            reStr += t2[::-1]
        if m > k:
            t3 = s[n*2*k : n*2*k+k]
            reStr += t3[::-1]
            reStr += s[n*2*k+k : ]

        return reStr

def test():
    sol = Solution()
    # s = "abcdefg";  k = 3
    s = "abcdefghij"; k =3
    # s = "q";    k =2
    print( sol.reverseStr(s, k))

if __name__ == "__main__":
    test()
'''
【总结】
1、算法设计应根据题目要求，逻辑清晰的进行分类讨论
2、增加测试用例
'''