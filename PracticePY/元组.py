#!/usr/bin/python
# -*- coding:utf8 -*-

tuple1 = (1,2,3)
print("tuple1:",tuple1)
print("type of tuple1:",type(tuple1))


tuple2 = ('甲','乙','丙')
print("tuple2:",tuple2)

temp = tuple1 + tuple2
print("tuple1+tuple2:",temp)

temp2 = tuple1[:1] + tuple2[1:]
print("tuple1[:1] + tuple2[1:]:",temp2)

print(1 in tuple2)
print("甲 in tuple2:",'甲' in tuple2)
print('丁' in tuple2)