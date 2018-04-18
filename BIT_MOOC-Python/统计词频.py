#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
用 Python 实现函数 count_words()，该函数输入字符串 s 和数字 n，返回 s 中 n 个出现频率最高的单词。
返回值是一个元组列表，包含出现次数最高的 n 个单词及其次数,
即 [(<单词1>, <次数1>), (<单词2>, <次数2>), ... ]，按出现次数降序排列。

您可以假设所有输入都是小写形式，并且不含标点符号或其他字符（只包含字母和单个空格）。
如果出现次数相同，则按字母顺序排列。

例如：print count_words("betty bought a bit of butter but the butter was bitter",3)

输出：[('butter', 2), ('a', 1), ('betty', 1)]

@author: ZHOU Heng
"""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    sList = s.split(sep = ' ')      # 拆分字符串，得到单词列表
    # sList.sort()        # 按字母顺序排序

    top = dict()        # 单词：次数 字典
    sSet = set(sList)
    for word in sSet:
        word_n = 0      # word 出现的次数
        for i in range( len(sList) ):
            if word == sList[i]:
                word_n += 1
            top[word] = word_n

    # print(top)
    topAll = list( top.items() )          # topAll 是列表类型

    # 按出现次数排序。如果出现次数相同，则按字母顺序排列。
    # topAll.sort( key = lambda x: x[1] , reverse = True )
    topAll.sort( key = lambda x:( -x[1], x[0] ) )
    # 成功了！！！！

    # print(type(topAll), topAll)

    return topAll


def test_run():
    """Test count_words() with some inputs."""
    print( count_words("cat bat mat cat bat cat", 3) )
    print( count_words("betty bought a bit of butter but the butter was bitter", 3) )
    print( count_words('london bridge is falling down falling down falling down london bridge is falling down my fair lady', 5))


if __name__ == '__main__':
    test_run()