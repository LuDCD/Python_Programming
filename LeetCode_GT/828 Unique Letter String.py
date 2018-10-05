#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
A character is unique in string S if it occurs exactly once in it.

For example, in string S = "LETTER", the only unique characters are "L" and "R".

Let's define UNIQ(S) as the number of unique characters in string S.

For example, UNIQ("LETTER") =  2.

Given a string S, calculate the sum of UNIQ(substring) over all non-empty substrings of S.

If there are two or more equal substrings at different positions in S, we consider them different.

Since the answer can be very large, retrun the answer modulo 10 ^ 9 + 7.



Example 1:
Input: "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:
Input: "ABA"
Output: 8
Explanation: The same as example 1, except uni("ABA") = 1.

@author: ZHOU Heng
"""

class Solution:
    def uniqNum(self, s):
        """
        :type s:str
        :rtype:int
        """

        nRe = 0
        sList = list(s)
        sList.sort()
        for i in range(len(s)):
            t = sList[i]
            if i == 0:
                if t != sList[i+1]:
                    nRe += 1
            elif i < len(s) -1:
                if t != sList[i-1] and t != sList[i+1]:
                    nRe += 1
            else:
                if t != sList[i-1]:
                    nRe += 1

        return nRe

    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        超时！！！！！
        """
        leg = len(S)

        sumUniqNum = leg
        # sumUniqNum = 0
        for step in range(2,leg+1):
            for i in range(leg):
                startIndex = i
                endIndex = startIndex + step
                if endIndex <= leg:
                    subString = S[startIndex:endIndex]
                    print( subString )
                    sumUniqNum += self.uniqNum(subString)

        return sumUniqNum




def test():
    sol = Solution()
    # print( sol.uniqueLetterString("ABA") )
    # print( sol.uniqueLetterString("ABC") )
    # print( sol.uniqueLetterString("") )
    # print( sol.uniqueLetterString( 'A' ))
    print( sol.uniqueLetterString( 'ABCC') )
    # print( sol.uniqNum('ABCCC') )


if __name__ == "__main__":
    test()



