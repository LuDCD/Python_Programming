#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
给定一个数字 n，找出可形成完整阶梯行的总行数。
n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:
n = 5
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.

示例 2:
n = 8
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3.

@author: ZHOU Heng
"""

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = int( (2*n)**0.5 )
        while cnt > 0:
            if (1+cnt)*cnt*0.5 <= n < (cnt+2)*(cnt+1)*0.5 :
                break
            else:
                cnt -= 1

        return cnt


def test():
    sol = Solution()
    print( sol.arrangeCoins(8) )
    print( sol.arrangeCoins(5) )
    print( sol.arrangeCoins(1) )
    print( sol.arrangeCoins(0) )


if __name__ == "__main__":
    test()



