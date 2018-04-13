#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。
整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。
网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

示例 :
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

答案: 16
解释: 它的周长是下面图片中的 16 个黄色的边：

@author: ZHOU Heng
"""

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len( grid )       # 行
        n = len( grid[0] )    # 列

        circ = 0

        for i in range( m ):
            circ += 4*sum( grid[i][::] )

        newGrid = []    # (m+2)*(n+2)矩阵

        for i in range( m + 2 ):
            if i == 0 or i == (m+1):
                newGrid.append( [0]*(n+2) )
            else:
                newGrid.append( [0] + grid[i-1] + [0] )

        sumOpen = 0
        for i in range(m):
            r = i + 1
            for j in range(n):
                # 上下左右
                c = j + 1
                if newGrid[r][c] == 1:
                    up = newGrid[r-1][c]
                    down = newGrid[r+1][c]
                    rig = newGrid[r][c+1]
                    lef = newGrid[r][c-1]
                    sumOpen += sum( [up, down, rig, lef] )

        return circ - sumOpen


def test():
    sol = Solution()
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [0,1,0,0]]
    print( sol.islandPerimeter( grid ) )


if __name__ == "__main__":
    test()

