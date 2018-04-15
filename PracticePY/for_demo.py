#!/usr/bin/python
# -*- coding:utf8 -*-

fou = 'FishC'
print("type of fou:",type(fou))
for i in fou :
   print(i,end=' ')

print('\n')

member = ['周恒','张三','信工实验室','zhouheng']  #嘎嘎嘎
for each in member :
    print(each,len(each))

range(2, 19, 3)

for i in range(5):
    i += 50         # 这个循环还是跑了5次！这里的 i += 50 并没有改变for循环中的 i
    print(i)

i = 0
for i in range(i,10):   # range(i,10)这个根本就改变不了迭代器，他还是第一次的迭代了10次
    i += 100
    print(i)