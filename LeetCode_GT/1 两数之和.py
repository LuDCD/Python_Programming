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
    def twoSum3(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leg = len(nums)
        for i in range(leg):
            value = nums[i]
            diff = target - value
            nums[i] = 'used'
            if diff in nums:
                idx = nums.index(diff)
                return [i, idx]

            # 恢复
            nums[i] = value


    def twoSum2(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 使用哈希映射
        # 根据已有数据创建字典
        leg = len(nums)
        hashMap = dict( zip(range(leg), nums) )
        # hashMap = dict( zip(nums, range(leg)) )  # 不行
        # 在字典dict中，key值是唯一的，且不可变；而value可以随意取值，且不唯一。
        for i in range(leg):
            value = nums[i]
            del hashMap[i]
            diff = target - value
            if diff in hashMap.values():
                # 如何按value找key
                idx = list(hashMap.keys())[list(hashMap.values()).index(diff)]
                # python3 文档，
                # 在你迭代的过程中如果没有发生对字典的修改，
                # 那么.keys() and .values 这两个函数返回的 dict-view对象总是保持对应关系。
                return [i, idx]



    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 时间复杂度O(N^2)
        
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
    nums = [2, 7, 11, 15];target = 9
    # nums  = [3, 3]; target = 6
    # nums = [-3,4,3,90]; target = 0
    # nums = [0,4,3,0];   target = 0

    s = Solution()
    a = s.twoSum(nums.copy(), target)
    a2 = s.twoSum2(nums.copy(), target)
    a3 = s.twoSum3(nums.copy(), target)
    print( a, a2 , a3)


if __name__ == "__main__":
    test()