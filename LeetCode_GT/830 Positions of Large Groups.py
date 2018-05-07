#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.
We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.


Example 1:
Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:
Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:
Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000

@author: ZHOU Heng
"""

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        startIndex = 0
        endIndex = 0
        posList = []
        i = 0
        while i < (len(S)-2):
            startIndex = i
            for j in range(i+1,len(S)):
                if S[j] == S[i]:
                    endIndex = j
                else:
                    break
            if endIndex-startIndex >= 2:
                i = endIndex
                posList.append( [startIndex, endIndex] )
            else:
                i += 1

        return posList



def test():
    sol = Solution()
    print( sol.largeGroupPositions("abbxxxxzzy") )
    print( sol.largeGroupPositions("abcdddeeeeaabbbcd") )
    print( sol.largeGroupPositions('a') )


if __name__ == "__main__":
    test()



