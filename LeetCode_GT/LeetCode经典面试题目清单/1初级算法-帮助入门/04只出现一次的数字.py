#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。
你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4

@author: ZHOU Heng
"""


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for e in nums:
            if nums.count(e) == 1:
                return e


def test():
    sol = Solution()
    nums = [4, 1, 2, 1, 2]
    n = sol.singleNumber(nums)
    print(n)


if __name__ == "__main__":
    test()
