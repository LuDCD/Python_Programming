#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个矩阵 A， 返回 A 的转置矩阵。
矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。



示例 1：
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]

示例 2：
输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]

提示：
    1 <= A.length <= 1000
    1 <= A[0].length <= 1000

@author: ZHOU Heng
"""

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rlen = len(A)
        clen = len(A[0])

        # A1 = [[0]*clen]*rlen  # 不对！
        # 这个方法很值得学习。我就的就不行！！
        A1 = [[0] * rlen for _ in range(clen)]
        # print(A1)

        # print("r:{},c:{}".format(rlen, clen))

        for i in range(clen):
            for j in range(rlen):
                A1[i][j] = A[j][i]

        return A1




def main():
    sol = Solution()
    print(sol.transpose( [[1,2,3],[4,5,6]] ))


if __name__ == "__main__":
    main()