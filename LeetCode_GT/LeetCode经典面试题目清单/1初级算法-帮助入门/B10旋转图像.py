#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
未解决。算法是参考网上的。
https://www.codeleading.com/article/62002595912/
https://www.itranslater.com/qa/details/2108594960353199104


给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。
请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

@author: ZHOU Heng
"""


class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        layer_count = size // 2

        for layer in range(0, layer_count):
            first = layer
            last = size - first - 1

            for element in range(first, last):
                offset = element - first

                top = matrix[first][element]
                right_side = matrix[element][last]
                bottom = matrix[last][last - offset]
                left_side = matrix[last - offset][first]

                matrix[first][element] = left_side
                matrix[element][last] = top
                matrix[last][last - offset] = right_side
                matrix[last - offset][first] = bottom
        print(matrix)


def test():
    sol = Solution()
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(sol.rotate(matrix))


if __name__ == "__main__":
    test()
