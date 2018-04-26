#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数应该返回 true。
如果每个元素都不相同，则返回 false。

@author: ZHOU Heng
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = 0
        nums.sort()
        for i in range( len(nums)-1 ):
            if nums[i] == nums[i+1]:
                flag = 1
                break

        return bool(flag)


def test():
    nums = []
    sol = Solution()
    print( sol.containsDuplicate(nums) )


if __name__ == "__main__":
    test()



