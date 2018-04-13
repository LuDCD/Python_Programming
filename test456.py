#!/usr/bin/env python
# -*- coding:utf8 -*-

# import os
# ss = os.getcwd()
# print(ss)

s = "abcdefg"
reList = []
t = s[0:4]
reList = reList + list( ''.join(t)[::-1] )
print(reList)