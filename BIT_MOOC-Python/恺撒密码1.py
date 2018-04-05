#!/usr/bin/env python
# -*- coding:utf8 -*-

a_ord = ord('a')

pList = []
for i in range(26):
    pList.append( chr(a_ord+i) )

pn = input()
cList = []
# print(pn)
for i in range( len(pn) ):
    if pn[i] in pList:
        pord = ord(pn[i])
        if ord(pn[i]) < (a_ord+23):
            cord = (pord+3)
            x = chr( cord )
            cList.append( x )
        else:
            cord = (pord-23)
            x = chr( cord )
            cList.append( x )
    else:
        cList.append(pn[i])

print( ''.join(cList) )