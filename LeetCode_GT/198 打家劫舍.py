#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，
计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = = 2 + 9 + 1 = 12 。

@author: ZHOU Heng
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 先对 nums 进行排序
        numsSorted = sorted( nums, reverse=True )

        # 奇数位加和偶数位加
        leng = len( nums )
        maxSum = max( sum( nums[0:leng:2] ), sum( nums[1:leng:2] ) )

        if leng == 1:
            return nums[0]

        tSum = 0
        for k in numsSorted:
            if k in nums:
                i = nums.index(k)
                print( nums )
                if i == 0:
                    if nums[i+1] != None:
                        tSum += k
                        nums[i] = None
                elif i == leng-1:
                    if nums[i-1] != None:
                        tSum += k
                        nums[i] = None
                elif nums[i-1] != None and nums[i+1] != None:
                    tSum += k
                    nums[i] = None

        maxSum = max( tSum, maxSum )

        return maxSum



def test():
    # nums = [5,6,5,1]
    # nums = [10,1,1,10,1]
    # nums = [0]
    nums = [6,3,10,8,2,10,3,5,10,5,3]
    # nums = []
    sol = Solution()
    print( sol.rob(nums) )


if __name__ == "__main__":
    test()
'''
算法有问题，明天再调！good, night!
'''


