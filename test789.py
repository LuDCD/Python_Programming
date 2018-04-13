#!/usr/bin/env python
# -*- coding:utf8 -*-


nums = [ [1,2], [3,4] ]

m = len(nums)
n = len( nums[0] )

newNum = []
for i in range(m):
    newNum += nums[i]

print(newNum)