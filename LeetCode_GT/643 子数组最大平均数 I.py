#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


注意:
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。

@author: ZHOU Heng
"""

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        startIndex = 0
        endIndex = startIndex + k
        leg = len(nums)
        maxSum = -10000
        while endIndex <= leg:

            t = sum( nums[startIndex:endIndex] )
            # print(t, '=', nums[startIndex:endIndex])
            if t > maxSum:
                maxSum = t
            startIndex += 1
            endIndex = startIndex + k

        return maxSum/k

def test():
    nums = [1,12,-5,-6,50,3];    k = 4
    sol = Solution()
    print( sol.findMaxAverage(nums, k) )
    print( sol.findMaxAverage([1], 1) )
    print( sol.findMaxAverage([-1], 1) )


if __name__ == "__main__":
    test()



