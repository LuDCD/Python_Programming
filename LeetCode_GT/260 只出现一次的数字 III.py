#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。
找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]

注意：
结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。

你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

@author: ZHOU Heng
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leg = len(nums)
        nums.sort()
        onlyOneList = []
        i = 0
        while i < leg-1:
            t = nums[i]
            if t == nums[i+1]:
                i = i+2
            else:
                onlyOneList.append(t)
                i += 1

        if nums[-1] != nums[-2]:
            onlyOneList.append( nums[-1] )

        return onlyOneList


def test():
    sol = Solution()
    print( sol.singleNumber([1,2,1,3,2,5]) )    # [3,5]
    print( sol.singleNumber([3,2,3,4,4,1]) )



if __name__ == "__main__":
    test()