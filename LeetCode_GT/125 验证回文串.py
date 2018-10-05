#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个字符串，验证它是否是回文串，只考虑【字母】和【数字字符】，可以忽略字母的大小写。
说明：本题中，我们将【空字符串】定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

@author: ZHOU Heng
"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lowStr = s.lower()
        clearStr = ''
        for e in lowStr:
            if 'a' <= e <= 'z':
                clearStr = clearStr + e
            else:
                try:
                    if isinstance( eval(e), int ):
                        clearStr = clearStr + e
                except:
                    pass


        flag = 0
        if clearStr == '' or clearStr == clearStr[::-1]:
            flag = 1

        return bool( flag )



def test():
    sol = Solution()
    print( sol.isPalindrome("A man, a plan, a canal: Panama") ) # True
    print( sol.isPalindrome('') )
    print( sol.isPalindrome("race a car") )     # False


if __name__ == "__main__":
    test()



