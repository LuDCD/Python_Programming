#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。
如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：
你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

@author: ZHOU Heng
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        flag = 1
        len_ran = len( ransomNote )

        magList = list( magazine )

        for i in range( len_ran ):
            k = ransomNote[i]
            if k in magList:
                magList[ magList.index(k) ] = None
            else:
                flag = 0
                break

        return bool(flag)

def test():
    sol = Solution()
    # print( sol.canConstruct( 'ac', 'ab') )
    # print( sol.canConstruct("", "a") )
    # print( sol.canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh") )
    print( sol.canConstruct( "fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))

if __name__ == "__main__":
    test()



