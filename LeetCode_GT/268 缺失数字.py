#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给出一个包含 0, 1, 2, ..., n 中 n 个数的序列，
找出 0 .. n 中没有出现在序列中的那个数。

案例 1
输入: [3,0,1]
输出: 2

案例 2
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

注意事项:
您的算法应该以线性复杂度运行。
你能否仅使用恒定的额外空间复杂度来实现它？

@author: ZHOU Heng
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len( nums )
        aList = [1]*(n+1)
        for k in nums:
            aList[k] = 0

        for i in range( n+1 ):
            if aList[i] == 1:
                return i

def test():
    # nums = [9,6,4,2,3,5,7,0,1]
    nums = [3,0,1]
    sol = Solution()
    print( sol.missingNumber(nums) )


if __name__ == "__main__":
    test()


