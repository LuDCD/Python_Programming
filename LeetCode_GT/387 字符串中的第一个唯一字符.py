#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.

注意事项：您可以假定该字符串只包含小写字母。

@author: ZHOU Heng
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        超时！！！
        """
        reIndex = -1

        for k in s:
            if s.count(k) == 1:
                reIndex = s.index(k)
                break

        return reIndex

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        reIndexSet = set()

        sSet = set( s )

        for k in sSet:
            if s.count(k) == 1:
                reIndexSet.add( s.index(k) )

        if reIndexSet == set():
            reIndexSet.add(-1)

        return min( reIndexSet )

def test():
    sol = Solution()
    print( sol.firstUniqChar2("leetcode") )
    print( sol.firstUniqChar2("loveleetcode") )


if __name__ == "__main__":
    test()



