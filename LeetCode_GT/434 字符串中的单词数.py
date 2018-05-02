#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:
输入: "Hello, my name is John"
输出: 5

@author: ZHOU Heng
"""

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        sList = s.split(' ')
        # 删除所有 '' 元素
        while 1:
            if '' in sList:
                sList.remove('')
            else:
                break

        return len( sList )



def test():
    s = "Hello, my name is John"
    sol = Solution()
    print( sol.countSegments(s) )
    print( sol.countSegments(' ') )
    print( sol.countSegments('  we   ef  ') )
    print( sol.countSegments( "love live! mu'sic forever" ) )

    s2 = "The one-hour drama series Westworld is a dark odyssey about the dawn of artificial consciousness and the evolution of sin. Set at the intersection of the near future and the reimagined past, it explores a world in which every human appetite, no matter how noble or depraved, can be indulged."
    print( sol.countSegments( s2 ))



if __name__ == "__main__":
    test()



