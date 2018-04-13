#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶节点的最长路径上的节点数。

案例：
给出二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回最大深度为 3 。

@author: ZHOU Heng
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = len(root) -1
        n = math.ceil( l / 4 )
        return n


def test():
    sol = Solution()


if __name__ == "__main__":
    test()
# 不清楚输入的是什么
# 暂时没思路，待定。