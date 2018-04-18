#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个大小为 n 的数组，找到其中的众数。
众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且数组中的众数永远存在。

@author: ZHOU Heng
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 超时！！！
        threshold = len(nums)//2    # 阈值
        numsSet = set( nums )

        frequency = {}      # 出现频次字典

        for k in numsSet:
            frequency[ str(k) ] = nums.count( k )

        for d in frequency:
            if frequency[d] > threshold:
                return eval( d )

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 不超时！！！
        threshold = len(nums)//2    # 阈值

        frequency = {}      # 出现频次字典（数：出现的次数）
        keyList = []        # 存储键

        for i in range( len(nums) ):
            k = nums[i]
            if k not in keyList:
                keyList += [k]
                frequency[ k ] = 1
            else:
                frequency[ k ] += 1

        for d in frequency:
            if frequency[d] > threshold:
                return d

def test():
    # nums = [1]
    nums = [1, 2, 3, 1, 1, 1, 1]

    sol = Solution()
    print( sol.majorityElement2(nums) )


if __name__ == "__main__":
    test()


