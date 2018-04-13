#!/usr/bin/env python
# -*- coding:utf8 -*-


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = len(s)
        if l < k:
            return s

        sList = list(s)
        # print(sList)

        n = l // k
        if n % 2 == 0:
            m = n // 2
        else:
            m = 1 + n // 2
        # print('m =',m)

        reList = []
        for i in range( m ):
            t = sList[i*2*k : i*2*k+k]
            reList += list( ''.join(t)[::-1] )
            reList += sList[i*2*k+k : i*2*k+2*k]
        del sList[ : m*2*k+2*k]
        reList += sList

        reStr = ''.join(reList)
        return reStr