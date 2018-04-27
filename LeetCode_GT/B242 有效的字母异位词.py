#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

例如，
s = "anagram"，t = "nagaram"，返回 true
s = "rat"，t = "car"，返回 false

注意:
假定字符串只包含小写字母。

提升难度:
输入的字符串包含 unicode 字符怎么办？你能能否调整你的解法来适应这种情况？

@author: ZHOU Heng
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag = 0    # 默认不是一个字母异位词
        ls = len(s)
        lt = len(t)

        # 先判断元素是否一样
        sList = list( s )
        tList = list( t )

        if sorted(s) == sorted(t):
            # 存放s、t字符串对应字母的 Unicode 差值
            flagList = [0]*ls
            for i in range(ls):
                flagList[i] = ord( s[i] ) - ord( t[i] )
            if flagList.count(0) == ls-1:
                flag = 1


        return bool(flag)



def test():
    s = "anagram";      t = "nagaram" #返回 true
    # s = "rat"，t = "car"，返回 false
    sol = Solution()
    print( sol.isAnagram(s, t) )

if __name__ == "__main__":
    test()

'''
未完
'''