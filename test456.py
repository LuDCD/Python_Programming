#!/usr/bin/env python
# -*- coding:utf8 -*-

# import os
# ss = os.getcwd()
# print(ss)

l = ['f1', 'f2']

def ff( s, l= [] ):
    l.append(s)

ff('X')
print(l)