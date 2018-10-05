#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:
输入: [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: [3,3,7,7,10,11,11]
输出: 10

注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。

@author: ZHOU Heng
"""

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leg = len(nums)
        i = 0
        while i < leg-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                singleNum = nums[i]
                break

        if i == leg-1:
            singleNum = nums[-1]

        return singleNum

def test():
    sol = Solution()
    print( sol.singleNonDuplicate([3,3,7,7,10,10,11,11,12]) )


if __name__ == "__main__":
    test()