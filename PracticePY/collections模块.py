#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
collections模块的使用简介。

我们都知道，Python拥有一些内置的数据类型，比如str, int, list, tuple, dict等，
collections模块在这些内置数据类型的基础上，提供了几个额外的数据类型：

1.namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
3.Counter: 计数器，主要用来计数
4.OrderedDict: 有序字典
5.defaultdict: 带有默认值的字典

@author: ZHOU Heng
"""


"""
 ========================== 3、Counter ===========================
计数器是一个非常常用的功能需求，collections也贴心的为你提供了这个功能。
"""
# 【例子1】
# 使用Counter模块统计一段句子里面所有【字符】出现次数
from collections import Counter

s = (
    """A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.""".lower()
)
c = Counter(s)
# 获取出现频率最高的5个字符。注意是【字符】，不是【单词】！
print("统计字符，出现最多的前五名：{}".format(c.most_common(5)))
# [(" ", 54), ("e", 32), ("s", 25), ("a", 24), ("t", 24)]

# 【例子2】
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)
# Counter({'blue': 3, 'red': 2, 'green': 1})

# 【例子3】
# 统计Hamlet的最常用单词。
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
print("前10个最常用单词{}".format(Counter(words).most_common(10)))