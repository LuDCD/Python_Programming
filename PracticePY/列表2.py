#!/usr/bin/python
# -*- coding:utf8 -*-

list1 = [123]
list2 = [123]
print("type of list1:",type(list1))
print("list1:",list1)
print("list2:",list2)

print(list1 > list2),

list3 = [23,456]
print("list3:",list3)
print("list1 > list3:",list1 > list3),

list4 = [23,456,7]
print("list4:",list4)
print("list3 == list4:", list3 == list4)

# "+"连接操作符
list34 = list3 + list4
print("list3 + list4:",list34)


# 分片“拷贝”的概念

list5 = [1,32,43,5,0,11,55]
print("list5:",list5)
list51 = list5  # 指向同一个实体
list52 = list5[:]# 复制一份
print("list51:",list51)
print("list52:",list52)

list5.sort()
print("list5:",list5)
print("list51:",list51)
print("list52:",list52)