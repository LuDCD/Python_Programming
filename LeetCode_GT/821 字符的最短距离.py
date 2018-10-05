#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个字符串 S 和一个字符 C。
返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:
输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

说明:
字符串 S 的长度范围为 [1, 10000]。
C 是一个单字符，且保证是字符串 S 里的字符。
S 和 C 中的所有字母均为小写字母。

@author: ZHOU Heng
"""

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        leg = len(S)
        distance = [0]*leg
        for i in range(leg):
            t = S[i]
            if t == C:
                distance[i] = 0
            else:
                dist1 = dist2 = leg+2
                headSubString = S[0:i][::-1]
                endSubString = S[i+1:]
                print(headSubString,'==',endSubString)
                if C in headSubString:
                    dist1 = headSubString.index(C) + 1
                if C in endSubString:
                    dist2 = endSubString.index(C) + 1

                distance[i] = min(dist1, dist2)

        return distance


def test():
    sol = Solution()
    S = "loveleetcodec"; C = 'e'
    print( sol.shortestToChar(S, C) )


if __name__ == "__main__":
    test()