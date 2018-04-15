#!/usr/bin/env python
# -*- coding:utf8 -*-

def f(n):
    n.sort()


n = [1,2,3,4,1,43,1,4,6,8,2,4]
f(n)
print( n )      # 传递的是索引，是指针
