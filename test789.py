#!/usr/bin/env python
# -*- coding:utf8 -*-

from pandas import Series, DataFrame
data = {'language': ['Java', 'PHP', 'Python', 'R', 'C#'],
            'year': [ 1995 ,  1995 , 1991   ,1993, 2000]}
frame = DataFrame(data)
frame['IDE'] = Series(['Intellij', 'Notepad', 'IPython', 'R studio', 'VS'])

print( 'VS' in frame['IDE'] )

print(frame['year'][2])