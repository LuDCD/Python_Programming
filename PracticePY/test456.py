#!/usr/bin/env python
# -*- coding:utf8 -*-

def reverse (s):
   return  reverse  (s[1:])+s[0]

a = 'abcdefghij'
b = reverse( a )
print(a)
print(b)