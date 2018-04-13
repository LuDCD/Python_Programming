#!/usr/bin/env python
# -*- coding:utf8 -*-

# import os
# ss = os.getcwd()
# print(ss)

mylist = [[1,5,6],[2,7,8],[3,9,10],[4,11,12]]
list1 = []
list2 = []
for l in mylist:
    list1 += [l[0]]
    list2 += l[1:]
print(list1)
print(list2)