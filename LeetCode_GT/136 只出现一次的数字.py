#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个整数数组，除了某个元素外其余元素均出现两次。
请找出这个只出现一次的元素。

备注：
你的算法应该是一个线性时间复杂度。 你可以不用额外空间来实现它吗？

@author: ZHOU Heng
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len( nums )

        aSet = set()      # 存放 nums 中所有元素
        bSet = set()      # 存放 aSet 中已经有的元素
        for i in range(l):
            t = nums[i]
            if t in aSet:
                bSet.add( t )
            else:
                aSet.add( t )

        return ( aSet - bSet ).pop()





def test():
    # nums = [1,2,2]
    nums = [1]
    sol = Solution()
    print( sol.singleNumber(nums) )


if __name__ == "__main__":
    test()


