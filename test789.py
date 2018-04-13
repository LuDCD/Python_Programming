#!/usr/bin/env python
# -*- coding:utf8 -*-


nums = [1,1,0,1,0,1]


sNum = ''

l = len(nums)
for i in range(l):
    sNum += str( nums.pop() )

nList = sNum.split('0')

print(set (nList) )