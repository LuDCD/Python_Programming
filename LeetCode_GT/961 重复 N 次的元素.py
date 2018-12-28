#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。


示例 1：
输入：[1,2,3,3]
输出：3

示例 2：
输入：[2,1,2,5,3,2]
输出：2

示例 3：
输入：[5,1,5,2,5,3,5,4]
输出：5


提示：

    4 <= A.length <= 10000
    0 <= A[i] < 10000
    A.length 为偶数

@author: ZHOU Heng
"""

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        N = len(A)//2
        for i in range(N+1):
            if A[i] == A[N+i-1]:
                return A[i]



def main():
    sol = Solution()
    print(sol.repeatedNTimes([5,1,5,2,5,3,5,4]))


if __name__ == "__main__":
    main()