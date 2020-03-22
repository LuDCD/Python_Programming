#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个整数数列，找出其中和为特定值的那两个数。
你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

@author: ZHOU Heng
"""

class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = sorted(nums)     # nums排序（从小到大）
        l1 = l2 = len(nums)
        # print(nums)

        cmpNum = [i-target for i in num]
        if 0 in cmpNum and target != 0:
            l2 = cmpNum.index(0)
        elif cmpNum[-1] > 0:
            for i in range(l1):
                if cmpNum[i] < 0 and cmpNum[i+1] >0:
                    l2 = i + 1
                    # print('l2',l2)
                    break
        if l2 != l1:
            l2 = l2+1

        for i in range( l2 ):
            for j in range(i+1,l2):
                if (num[i] + num[j]) == target:
                    p = nums.index(num[i])
                    nums[p] = None
                    q = nums.index(num[j])
                    return [p,q]

def test():
    # nums = [2, 7, 11, 15];target = 9
    # nums  = [3, 3]; target = 6
    # nums = [-3,4,3,90]; target = 0
    nums = [0,4,3,0];   target = 0

    s = Solution()
    a = s.twoSum(nums, target)
    print( a )


if __name__ == "__main__":
    test()