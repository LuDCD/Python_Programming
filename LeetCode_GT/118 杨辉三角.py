#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

@author: ZHOU Heng
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        YHtriangle = [[1], [1,1]]
        leg = len(YHtriangle)
        while numRows - leg:
            # 取最后一行
            lastList = YHtriangle[-1]
            # 新产生一行的个数
            rnum = len( lastList ) + 1
            # 全填1
            newList = [1]*rnum

            for i in range(1,rnum-1):
                newList[i] = lastList[i-1] + lastList[i]

            YHtriangle.append( newList )
            leg += 1

        return YHtriangle



def test():
    sol = Solution()
    # print( sol.generate(5) )
    # print( sol.generate(1) )
    # print( sol.generate(0) )
    print( sol.generate(34) )


if __name__ == "__main__":
    test()