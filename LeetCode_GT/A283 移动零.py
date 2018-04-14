#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。

注意事项:
必须在原数组上操作，不要为一个新数组分配额外空间。
尽量减少操作总数。

@author: ZHOU Heng
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums1 = nums
        l = len( nums1 )
        for i in range(l):
            if nums1[i] == 0:
                nums1[i] = None
                nums1.append(0)

        nums = [k for k in nums1 if k != None]

        # for i in range(len(nums)):
        #     if nums[i] == None:
        #         del nums[i]


        return nums

def test():
    sol = Solution()
    nums = [0, 1, 0, 3, 0, 12, 13]
    # nums = [0,0,1]
    print( sol.moveZeroes(nums) )


if __name__ == "__main__":
    test()

'''
由于涉及到python的内存操作和地址处理，暂无思路。
虽然功能实现了，但操作了两块内存。
'''

