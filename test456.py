#!/usr/bin/env python
# -*- coding:utf8 -*-

# import os
# ss = os.getcwd()
# print(ss)

ops = ['5',"-2","4","C","D","9","+","+"]
l = len( ops )
for i in range( l ):
    t = ops[i]
    if t not in ['C', 'D', '+']:
        ops[i] = eval(t)
print(ops)