#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

示例 2 :
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。

注意：
s.length 在1到50,000之间。
s 只包含“0”或“1”字符。

@author: ZHOU Heng
"""

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        reN = 0         # 子串个数，返回值。
        l = len( s )

        sonList = []        # 存放子串

        for i in range(l-1):
            ts = s[i]       # 栈
            current_n = 1   # 标明栈底那种元素的个数
            other_n = 0      # 另一种元素的个数

            category = 1        # category=1，说明字符串s 中目前只有一种元素，另一种元素还可以进去，

            for j in range(i+1, l):
                # 如果只有一种元素
                if category == 1:
                    if s[j] == ts[-1]:      # 如果元素和栈顶的元素相同，则进栈
                        ts += s[j]          # 进栈
                        current_n += 1
                    else:
                        ts += s[j]          # 在只有一种元素的情况下，当前元素和栈顶元素不同。
                                            # 进栈，并判断是否可以输出了
                        category = 2        # 种类变 2
                        other_n += 1

                        # 判断是否可以输出了
                        if current_n == other_n:
                            reN += 1
                            sonList.append( ts )
                            break

                else:# 如果有两种元素
                    if s[j] == ts[-1]:      # 如果元素和栈顶的元素相同，则进栈
                        other_n += 1

                        # 判断是否可以输出了
                        if current_n == other_n:
                            reN += 1
                            sonList.append( ts )
                            break
                    else:
                        # 有两种元素，当前元素和栈顶的元素不相同，
                        # 则没有了，不找了，结束当前循环
                        break

        # print( sonList )

        return reN

def test():
    # s = "00110011"
    s = "10101"
    sol = Solution()
    print( sol.countBinarySubstrings(s) )


if __name__ == "__main__":
    test()


'''
https://leetcode-cn.com/problems/count-binary-substrings/description/
超时了！爆炸！！！！
'''