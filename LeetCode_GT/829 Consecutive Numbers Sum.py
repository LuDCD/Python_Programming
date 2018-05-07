#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Given a positive integer N, how many ways can
we write it as a sum of consecutive positive integers?

Example 1:
Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3

Example 2:
Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: 1 <= N <= 10 ^ 9.

@author: ZHOU Heng
"""

class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        超时了！！！

        规律：
        N/k = m + 余数
        当 k 为奇数时，余数 = 0
        当 k 为偶数时。余数 = (k-1)!
        即 N = m*k + 余数
        """
        nRe = 1
        for k in range(2,N):
            # 如果 i 为奇数
            if k % 2 == 1:
                if N % k == 0:
                    nRe += 1
            else:
                m = N // k
                if N - m*k == sum( range(k) ):
                    nRe += 1

        return nRe





def test():
    sol = Solution()
    print( sol.consecutiveNumbersSum(9) )
    print( sol.consecutiveNumbersSum(5) )
    print( sol.consecutiveNumbersSum(15) )
    print( sol.consecutiveNumbersSum(3749) )
    print( sol.consecutiveNumbersSum(3) )
    print( sol.consecutiveNumbersSum(8480) )
    print( sol.consecutiveNumbersSum(21) )


if __name__ == "__main__":
    test()



