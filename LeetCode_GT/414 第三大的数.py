#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个非空数组，返回此数组中第三大的数。
如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:
输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.

示例 2:
输入: [1, 2]
输出: 2
解释: 第三大的数不存在, 所以返回最大的数 2 .

示例 3:
输入: [2, 2, 3, 1]
输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

@author: ZHOU Heng
"""

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        aSet = set(nums)
        numSet = list(aSet)
        numSet.sort(reverse=True)
        if len(aSet) < 3:
            return numSet[0]
        else:
            return numSet[2]


def test():
    sol = Solution()
    print( sol.thirdMax([2, 2, 3, 1]) )
    print( sol.thirdMax([1, 2]) )   # 2


if __name__ == "__main__":
    test()