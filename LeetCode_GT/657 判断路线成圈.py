#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
初始位置 (0, 0) 处有一个机器人。
给出它的一系列动作，判断这个机器人的移动路线是否形成一个圆圈，
换言之就是判断它是否会移回到原来的位置。

移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。
机器人有效的动作有 R（右），L（左），U（上）和 D（下）。
输出应为 true 或 false，表示机器人移动路线是否成圈。

示例 1:
输入: "UD"
输出: true

示例 2:
输入: "LL"
输出: false

@author: ZHOU Heng
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        z = {"U":1+0j, "D":-1+0j, "R":1j, "L":-1j}
        # print(z)
        n = 0
        for k in moves:
            n = z[k] + n

        if n == 0:
            flag = True
        else:flag = False

        return flag

def test():
    s = Solution()
    # moves = "LL"
    moves = "UD"
    print( s.judgeCircle(moves) )


if __name__ == "__main__":
    test()