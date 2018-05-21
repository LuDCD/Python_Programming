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
        numZoers = 0    # 0的个数
        leg = len( nums )
        nums1 = nums.copy()
        # print( nums1 )
        nums.clear()
        # print( nums1 )

        for i in range(leg):
            if nums1[i] == 0:
                numZoers += 1
            else:
                nums.append( nums1[i] )

        nums += [0]*numZoers


def test():
    sol = Solution()
    nums = [0, 1, 0, 3, 0, 12, 13]
    # nums = [0,0,1]
    sol.moveZeroes(nums)
    print( nums )


if __name__ == "__main__":
    test()

'''
由于涉及到python的内存操作和地址处理，暂无思路。
虽然功能实现了，但操作了两块内存。
'''

