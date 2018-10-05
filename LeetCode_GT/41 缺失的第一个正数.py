#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1

说明:
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

@author: ZHOU Heng
"""

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序
        nums.sort(reverse=True)

        # 标记非正数
        endIndex = None
        for i in range(len(nums)):
            if nums[i] <= 0:
                endIndex = i
                break

        if endIndex != None:
            nums = nums[:endIndex]


        for i in range(1,len(nums)+2):
            if i not in nums:
                return i



def test():
    sol = Solution()
    print( sol.firstMissingPositive([7,8,9,11,12]) )
    print( sol.firstMissingPositive([3,4,6,5]) )
    print( sol.firstMissingPositive([1,2,0]) )
    print( sol.firstMissingPositive([]) )
    print( sol.firstMissingPositive([1,0]) )


if __name__ == "__main__":
    test()



