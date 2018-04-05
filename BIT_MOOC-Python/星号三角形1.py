#!/usr/bin/env python
# -*- coding:utf8 -*-

n = int( input() )

for i in range(n//2 + 1):
    b = int( (n-2*i-1)/2 )
    x = int( 2*i+1 )
    print( "{0}{1}{0}".format( ' '*b, '*'*x ) )