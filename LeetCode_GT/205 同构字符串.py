#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:
输入: s = "egg", t = "add"
输出: true

示例 2:
输入: s = "foo", t = "bar"
输出: false

示例 3:
输入: s = "paper", t = "title"
输出: true

说明:
你可以假设 s 和 t 具有相同的长度。

@author: ZHOU Heng
"""

class Solution(object):
    def Transformation(self, s, t):
        # 查看 s 中有多少种字母
        sSet = set( s )

        # 建立 s - t 字母对应字典
        corrDict = dict()
        for k in sSet:
            if k not in corrDict.keys():
                sIndex = s.index(k)
                corrDict[k] = t[sIndex]

        # 现在根据对应关系改写 s
        newS = ''
        for k in s:
            newS = newS + corrDict[k]

        return newS

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        newS = self.Transformation(s, t)
        newT = self.Transformation(t, s)

        flag = 0
        if newS == t and newT == s:
            flag = 1

        return bool(flag)




def test():
    s = "paper";        t = "title"
    # s = "foo";      t = "bar"
    # s = 'ab';       t = 'aa'
    sol = Solution()
    print( sol.isIsomorphic(s, t) )


if __name__ == "__main__":
    test()



