#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1。

示例 1:
输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

注意:
输入数组的长度不会超过 10000。

@author: ZHOU Heng
"""

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 当nums为空列表时
        if nums == []:
            return nums

        # nums 非空时
        M = max( nums )
        l = len( nums )
        reList = []
        for i in range(l):
            flag = 0    # 是否找到（即每一位的找数操作是否完成）
            t = nums[i]
            if t == M:
                reList.append( -1 )
                flag = 1
                continue

            # 往后找
            for j in range(i, len(nums)):
                if nums[j] > t:
                    reList.append( nums[j] )
                    flag = 1
                    break

            # 往前找
            if flag == 0:
                for j in range(i):
                    if nums[j] > t:
                        reList.append( nums[j] )
                        flag = 1
                        break

        return reList

def test():
    num = [1,2,1,3]
    # num = []
    # 极端例子大数非常多且降序

    sol = Solution()
    print( sol.nextGreaterElements(num) )


if __name__ == "__main__":
    test()
'''
https://leetcode-cn.com/problems/next-greater-element-ii/description/
超时，再议。
思路：
1、找出一个比他大的。排序预处理。
2、判断这个比他大的数，在列表中是否唯一。
3、如果唯一：则判断在其前还是后，遍历查找。
4、如果不唯一：难办。
'''
