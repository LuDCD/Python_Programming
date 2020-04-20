#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

@author: ZHOU Heng
"""


class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        leg = len(nums)
        idx = 0
        for i in range(leg):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx = idx + 1
        nums[idx:] = [0] * (leg - idx)
        print(nums)


def test():
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    print()


if __name__ == "__main__":
    test()
