#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。]

返回使 A 中的每个值都是唯一的最少操作次数。

示例 1:

输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
示例 2:

输入：[3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
提示：

0 <= A.length <= 40000
0 <= A[i] < 40000

@author: ZHOU Heng

不对。20200322
"""


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        natural_number = [i+1 for i in range(max(A))]
        set_A = set(A)
        A_repeat = sorted(A)  # 保留A中重复元素
        for v in set_A:
            A_repeat.remove(v)
            natural_number.remove(v)

        # 去除自然数列表中比较小的数
        for v in natural_number:
            if v < A_repeat[0]:
                natural_number.remove(v)

        legA = len(A_repeat)
        legNat = len(natural_number)
        moveLen = 0
        if legA != 0:
            if legNat >= legA:
                for i in range(legA):
                    dif = min(natural_number) - A_repeat[i]
                    if dif > 0:
                        moveLen = moveLen + dif
                        natural_number.remove(min(natural_number))
                    else:
                        moveLen = moveLen + legA - i
                        break

            else:
                moveLen = moveLen + legA

        return moveLen




def test():
    # nums = [3,2,1,2,1,7]  # 6
    # nums = [1,2,2,7,7]  # 2
    nums = [1,2,2]  # 1

    s = Solution()
    a = s.minIncrementForUnique(nums)
    print( a )


if __name__ == "__main__":
    test()
