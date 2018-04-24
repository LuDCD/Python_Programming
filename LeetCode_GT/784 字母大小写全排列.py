#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。
返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]

注意：
S 的长度不超过12。
S 仅由数字和字母组成。

@author: ZHOU Heng
"""

class Solution(object):
    def spliteList(self, alist):
        flag = 0    # 判断是否还含有两个字母的元素
        for i in range(len(alist)):
            k = alist[i]
            if len(k) == 2:
                flag = 1
                list1 = alist[:i] + [k[0].lower()] + alist[i+1:]
                list2 = alist[:i] + [k[0].upper()] + alist[i+1:]
                break

        if flag == 0:
            return alist
        else:
            return list1, list2


    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        sList = list( S )
        letterNum = 0
        for i in range(len(S)):
            k = sList[i]
            if 'A'<= k <= 'z':
                letterNum += 1  # 统计一下字母的个数
                sList[i] = k.lower() + k.upper()

        allList = []
        allList.append( sList )
        while len( allList ) != 2**letterNum:
            l = len( allList )
            for i in range(l):
                list1 = allList[i]
                if len( list1 ) != len( ''.join(list1)):
                    del allList[i]
                    l1, l2 = self.spliteList( list1 )
                    allList.append( l1 )
                    allList.append( l2 )
        l = len( allList )
        for i in range(l):
            allList[i] = ''.join( allList[i] )

        return allList


def test():
    # S = "a1b2"
    # S = "12345"
    S = "3z4"
    sol = Solution()
    print( sol.spliteList( ['aA',1,2] ) )
    print( sol.letterCasePermutation(S) )


if __name__ == "__main__":
    test()



