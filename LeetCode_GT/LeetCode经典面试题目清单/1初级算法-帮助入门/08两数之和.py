#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。
但是，数组中同一个元素不能使用两遍。



示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

@author: ZHOU Heng
"""


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = []
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums[i + 1:]:
                nums[i] = None
                idx.append(i)
                idx.append(nums.index(dif))
                return idx


def test():
    sol = Solution()
    nums = [2, 2]
    target = 4
    idx = sol.twoSum(nums, target)
    print(idx)


if __name__ == "__main__":
    test()
