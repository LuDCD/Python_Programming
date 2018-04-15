#!/usr/bin/python
# -*- coding:utf8 -*-


# 准备知识
# 使用 split() 方法将字符串中的每个单词分开，得到独立的单词
# e.g.
# lyric = 'The night begin to shine, the night begin to shine'
# words = lyric.split()
# print(words)

path = './Walden.txt'
with open(path,'r') as text:
    words = text.read().split()
    # print(words)
    for word in words:
        print('{}-{} times'.format(word,words.count(word)))