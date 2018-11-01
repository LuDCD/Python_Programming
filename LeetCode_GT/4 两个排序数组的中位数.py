#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 不同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]

中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5



@author: ZHOU Heng
"""

# 引用numpy模块
import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 1、numpy法
        #求数组a的中位数
        # med1 = np.median(nums1)
        # med2 = np.median(nums2)
        # return (med1+med2)/2

        # 普通方法
        res = nums1 + nums2
        res.sort()
        n = len(res)//2
        return res[n] if len(res)%2 ==1 else  (res[n]+res[n-1])/2






def main():
    sol = Solution()
    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # nums1 = [1, 3]
    # nums2 = [2]
    # nums1 = [1, 3]
    # nums2 = []
    nums1 = [3]
    nums2 = [-2,-1]
    print(sol.findMedianSortedArrays(nums1, nums2))


if __name__ == "__main__":
    main()