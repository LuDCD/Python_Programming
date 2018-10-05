#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤纪录判断他是否会被奖赏。

示例 1:
输入: "PPALLP"
输出: True

示例 2:
输入: "PPALLL"
输出: False

@author: ZHOU Heng
"""

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leg = len(s)
        numA = s.count('A')
        flag = 1
        if numA > 1:
            flag = 0
        elif leg >= 3:
            for i in range( leg-2 ):
                if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                    flag = 0
                    break

        return bool(flag)


def test():
    sol = Solution()
    print( sol.checkRecord("PPALLP") )
    print( sol.checkRecord("PPALLL") )
    print( sol.checkRecord("L") )


if __name__ == "__main__":
    test()