#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
File function

@author: ZHOU Heng
"""

class Solution(object):
    def pivotIndex2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        超时！！！
        """
        leg = len(nums)
        pivIndex = -1
        for i in range(leg):
            if i == 0:
                if sum(nums[1:]) == 0:
                    pivIndex = 0
                    break
            elif i < leg-1:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    pivIndex = i
                    break
            else:
                if sum(nums[:leg-1]) == 0:
                    pivIndex = leg - 1
                    break

        return pivIndex

    def pivotIndex(self, nums):
        leg = len(nums)
        pivIndex = -1
        strSum = 0
        endSum = sum(nums[1:])
        for i in range(leg):
            if i == 0:
                if endSum == 0:
                    pivIndex = 0
                    break
            elif i < leg-1:
                strSum = strSum + nums[i-1]
                endSum = endSum - nums[i]
                if strSum == endSum:
                    pivIndex = i
                    break
            else:
                if sum(nums[:-1]) == 0:
                    pivIndex = i
                    break

        return pivIndex

def main():
    sol = Solution()
    print(sol.pivotIndex(nums = [1, 2, 3]))     # -1
    print(sol.pivotIndex(nums = [1, 7, 3, 6, 5, 6]))    # 3
    print(sol.pivotIndex([-1,-1,-1,0,1,1]))         # 0
    print(sol.pivotIndex([-1,-1,1,1,0,0]))      # 4
    print(sol.pivotIndex([-1,-1,0,1,1,0]))  # 5


if __name__ == "__main__":
    main()