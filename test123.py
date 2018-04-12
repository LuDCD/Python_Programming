#!/usr/bin/python
# -*- coding:utf8 -*-

# import numpy as np
# a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# print( a.shape )
# print(a[[2]].sum())

words = ["abcd", "dcba", "lls", "s", "sssll"]

a = words[0][::-1]
print(a)
print(a == words[1], a+words[0])