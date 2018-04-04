#!/usr/bin/env python
# -*- coding:utf8 -*-

# 1 米 = 39.37 英寸

numlist = input()
if numlist[-1] in ['m']:
    num_in = eval(numlist[:-1])*39.37
    print('{:.3f}in'.format(num_in))
else:
    num_m = eval(numlist[:-2])/39.37
    print('{:.3f}m'.format(num_m))
