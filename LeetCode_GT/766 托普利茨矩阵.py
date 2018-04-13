#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

示例 1:
输入: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
输出: True
解释:
1234
5123
9512

在上面这个矩阵中, 对角线分别是 "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", 各条对角线上的所有元素都相同, 因此答案是True。

示例 2:
输入: matrix = [[1,2],[2,2]]
输出: False
解释: 对角线, 比如: "[1, 2]" 上有不同的元素。

注意:
matrix (矩阵)是一个包含整数的二维数组。
matrix 的行数和列数均在 [1, 20]范围内。
matrix[i][j] 包含的整数在 [0, 99]范围内。

@author: ZHOU Heng
"""

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len( matrix )       # 行
        n = len( matrix[0] )    # 列
        # print(m,n)
        newMat = []
        for i in range(m):
            newMat.append( [None]*(m-1-i) + matrix[i] + [None]*i )    # 草稿纸上算清楚( 用0填充有麻烦，因为本来可能含0 )

        # print(newMat)

        m2 = len( newMat )
        n2 = len( newMat[0] )

        flag = 1

        # # 首两行
        # cmp1 = newMat[0]
        # cmp2 = newMat[-1]

        for i in range( 1, m2 ):   # 遍历行
            blist = newMat[i-1]     # 上一行
            clist = newMat[i]       # 当前行
            if flag == 0:
                    break
            for j in range( n2 ):   # 遍历列
                if clist[j] != None:
                    if blist[j] != None and clist[j] != blist[j]:   # 和上一行比较
                        flag = 0
                        break

        return bool( flag )


def test():
    sol = Solution()
    # matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    matrix = [[1,2],[2,2]]
    # matrix = [[0,33,98],[34,22,33]]
    # matrix = [[44,35,39],[15,44,35],[17,15,44],[80,17,15],[43,80,0],[77,43,80]]
    print( sol.isToeplitzMatrix(matrix) )


if __name__ == "__main__":
    test()


