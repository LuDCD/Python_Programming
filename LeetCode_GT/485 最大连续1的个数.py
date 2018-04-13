#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

注意：
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

@author: ZHOU Heng
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路
        将[1,1,0,1,1,1]转换成字符串'110111'，再以'0'为分割符，分成['11', '111']
        再将['11', '111']变成集合set，算的集合元素长度的列表[2, 3]，返回集合元素长度的列表的最大值
        '''

        sNum = ''

        l = len(nums)
        for i in range(l):
            sNum += str( nums.pop() )

        nList = sNum.split('0')

        renSet = set(nList)
        renList = []
        for k in renSet:
            renList.append( len(k) )

        return max( renList )



def test():
    sol = Solution()
    nums = [0,1,0,1,0,1,1,1,0,1,0,1,1,0]
    print( sol.findMaxConsecutiveOnes(nums) )


if __name__ == "__main__":
    test()

