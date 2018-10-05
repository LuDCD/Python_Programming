#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。
找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。
你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,3,2]
输出: 3

示例 2:
输入: [0,1,0,1,0,1,99]
输出: 99

@author: ZHOU Heng
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leg = len(nums)
        nums.sort()

        i = 0
        while i < leg-1:
            if nums[i] == nums[i+1]:
                i = i+3
            else:
                onlyOne = nums[i]
                break

        if leg == 1:
            onlyOne = nums[-1]
        elif nums[-1] != nums[-2]:
            onlyOne = nums[-1]

        return onlyOne


def test():
    sol = Solution()
    print( sol.singleNumber([0,1,0,1,0,1,99]) )
    print( sol.singleNumber([2,2,3,2]) )
    print( sol.singleNumber([1]) )


if __name__ == "__main__":
    test()