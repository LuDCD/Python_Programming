#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

例如，
给定数组 [1,1,1,2,2,3] , 和 k = 2，返回 [1,2]。

注意：
你可以假设给定的 k 总是合理的，1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

@author: ZHOU Heng
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numsDict = dict()
        for e in nums:
            if e in numsDict:
                numsDict[e] += 1
            else:
                numsDict[e] = 1

        numsDictSortedList = sorted( numsDict.items(), key=lambda x:x[1], reverse=True )
        topKnum = []
        for i in range(k):
            # print( i )
            topKnum.append(numsDictSortedList[i][0])

        # print( numsDict )
        return topKnum


def test():
    sol = Solution()
    print( sol.topKFrequent([1,1,1,2,2,3], 2) )
    print( sol.topKFrequent([1], 1) )
    print( sol.topKFrequent([1,2], 2) )


if __name__ == "__main__":
    test()



