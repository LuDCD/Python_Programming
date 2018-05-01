#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:
输入:"tree"
输出:"eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

示例 2:
输入:"cccaaa"
输出:"cccaaa"
解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。

示例 3:
输入:"Aabb"
输出:"bbAa"
解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。

@author: ZHOU Heng
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        sDict = dict()
        for k in s:
            if k in sDict:
                sDict[k] += 1
            else:
                sDict[k] = 1

        sDictList = sorted(sDict.items(), key = lambda k: k[1], reverse=True)

        reStr = ''
        for k in sDictList:
            reStr = reStr + k[0]*k[1]

        return reStr



def test():
    sol = Solution()
    print( sol.frequencySort("Aabb") )
    print( sol.frequencySort("cccaaa") )
    print( sol.frequencySort("tree") )


if __name__ == "__main__":
    test()



