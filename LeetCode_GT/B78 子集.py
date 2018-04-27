#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

@author: ZHOU Heng
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subList = [ [] ]
        l = len(nums)

        nums1 = nums.copy()
        for i in range( l ):
            t = []
            for k in nums1:
                t.append(k)
                # print(t)
                # subList.append( t )     # 不对
                subList.append( t.copy() )
                # print( 'subList', subList )

            del nums1[0]

        if l <= 2:
            return subList
        else:
            nums2 = nums.copy()
            for i in range( 1, l-1 ):
                t2 = []
                for j in range(i+1, l-1):
                    t2 += (nums2[:i] + nums2[j])
                    subList.append( t2.copy() )

            return subList

def test():
    nums = [1,2,3]
    sol = Solution()
    print( sol.subsets(nums) )


if __name__ == "__main__":
    test()
'''
未完待续
'''


