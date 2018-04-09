#!/usr/bin/env python
# -*- coding:utf8 -*-

s = "betty bought a bit of butter but the butter was bitter"
sList = s.split(sep = ' ')      # 拆分字符串，得到单词列表
#  sList.sort()        # 按字母顺序排序

top_n = []
top = dict()
sSet = set(sList)
for word in sSet:
    word_n = 1      # word 出现的次数
    for i in range( len(sList) ):
        if word == sList[i]:
            word_n += 1
        top[word] = word_n

print(top)

aa = sorted( top.items(), key = lambda x:x[1], reverse = False )

print('fiest',aa)
print(aa.pop())
print('second',aa)
print(aa.value(2))