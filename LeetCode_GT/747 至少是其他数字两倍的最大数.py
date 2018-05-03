#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
在一个给定的数组nums中，【总是存在】一个最大元素 。
查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大元素的索引，否则返回-1。

示例 1:
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.

示例 2:
输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.

提示:
nums 的长度范围在[1, 50].
每个 nums[i] 的整数范围在 [0, 99].

@author: ZHOU Heng
"""

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reIndex = -1
        leg = len(nums)
        if leg == 1:
            reIndex = 0
        else:
            numsSorted = sorted(nums, reverse=True)
            if numsSorted[0] >= 2*numsSorted[1]:
                reIndex = nums.index( numsSorted[0] )

        return reIndex


def test():
    # nums = [1, 2, 3, 4]
    nums = [3, 6, 1, 0]
    sol = Solution()
    print( sol.dominantIndex( nums ) )


if __name__ == "__main__":
    test()



