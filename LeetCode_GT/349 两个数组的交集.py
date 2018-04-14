#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定两个数组，写一个函数来计算它们的交集。

例子:
给定 num1= [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

提示:
每个在结果中的元素必定是唯一的。
我们可以不考虑输出结果的顺序。

@author: ZHOU Heng
"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        reSet = set(nums1) & set(nums2)

        return [k for k in reSet]

def test():
    num1= [1, 2, 2, 1]
    nums2 = [2, 2, 1]
    sol = Solution()
    print( sol.intersection(num1, nums2))


if __name__ == "__main__":
    test()

