#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:
输入: [1,2,3,1], k = 3
输出: true

示例 2:
输入: [1,0,1,1], k = 1
输出: true

示例 3:
输入: [1,2,1], k = 0
输出: false

@author: ZHOU Heng
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        leg = len(nums)
        flag = 0
        i = 0
        while i+k+1 <= leg:
            t = nums[i]
            if nums[i:i+k+1].count(t) > 1:
                flag = 1
                break
            i += 1

        return bool(flag)



def test():
    sol = Solution()
    nums = [1, 2, 3, 1];   k = 3
    print( sol.containsNearbyDuplicate(nums, k) )
    print( sol.containsNearbyDuplicate([1,0,1,1], k = 1))   # True
    print( sol.containsNearbyDuplicate([1,2,1], k = 0) )    #flase
    print( sol.containsNearbyDuplicate([1,2], k=2) )


if __name__ == "__main__":
    test()