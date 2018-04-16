#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

1 全部字母都是大写，比如"USA"。
2 单词中所有字母都不是大写，比如"leetcode"。
3 如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。

@author: ZHOU Heng
"""

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 思路判断有几个大写字母
        flag = 0    # 显示word是否符合条件。默认不符合。
        num = 0
        for w in word:
            if 'A' <= w <= 'Z':
                num += 1

        if num == 1 and 'A' <= word[0] <= 'Z' or num == 0 or num == len(word):
            flag = 1

        return bool( flag )







def test():
    word = "FlaG"
    # wList = str22listGT.str2list(word)
    # print( wList )
    sol = Solution()
    print( sol.detectCapitalUse(word) )


if __name__ == "__main__":
    test()


