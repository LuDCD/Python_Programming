#!/usr/bin/env python
# -*- coding:utf8 -*-


# 编写一个程序，计算输入数字N的0次方到5次方结果，并依次输出这6个结果，输出结果间用空格分隔。
# 其中：N是一个整数或浮点数。

a = eval( input() )
list1 = list()

if isinstance(a,int):
    list1.append(1)
else:list1.append(1.0)

for i in range(1,6):
  b = list1[i-1]*a
  list1.append(b)
  print( list1[i-1], end=' ' )

print(list1[5])