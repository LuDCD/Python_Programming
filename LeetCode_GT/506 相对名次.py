#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。
前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:

输入: [10,3,8,9,4]
输出: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
解释: 前三名运动员的成绩为前三高的，
因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
提示:

N 是一个正整数并且不会超过 10000。
所有运动员的成绩都不相同。

@author: ZHOU Heng
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        numSorted = sorted(nums, reverse=True)

        for i in range(len(nums)):
            t = numSorted[i]
            k = nums.index(t)
            if i in [0,1,2]:
                if i == 0:
                    nums[k] = "Gold Medal"
                elif i == 1:
                    nums[k] = "Silver Medal"
                else:
                    nums[k] = "Bronze Medal"
            else:
                nums[k] = str(i+1)

        return nums


def test():
    nums = [10,3,8,9,4]
    sol = Solution()
    print( sol.findRelativeRanks(nums) )


if __name__ == "__main__":
    test()



