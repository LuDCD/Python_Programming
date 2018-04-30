#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个【非负整数】组成的【非空】数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个【整数不会以零开头】。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

@author: ZHOU Heng
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strDigits = ''
        for k in digits:
            strDigits = strDigits + str(k)

        newDigits = eval( strDigits ) + 1

        return [ eval(i) for i in str(newDigits) ]



def test():
    # digits = [4,3,2,9]
    digits = [ 9, 9 ]
    sol = Solution()
    print( sol.plusOne(digits) )


if __name__ == "__main__":
    test()



