#!/usr/bin/python
# -*- coding:utf8 -*-

# 详见鱼C论坛
# http://bbs.fishc.com/forum.php?mod=viewthread&tid=38992&extra=page%3D1%26filter%3Dtypeid%26typeid%3D403


aStr = 'zhouheng xingongshiyanshi'
bStr = "zhhhhh" #双引号、单引号都可以表示字符串，Python中没有字符类型！。

print("aStr:",aStr)
print("bStr:",bStr)

cStr = 'i\tlove\tyou'
cStr.expandtabs(4)
print("cStr:",cStr)
print(cStr.find( 'you' ))

dStr = 'aaaaaaaahhhhhhhhhhhhhhhhhaaaaaaaa'
eStr = dStr.translate(dStr.maketrans('a','z'))
print(eStr)