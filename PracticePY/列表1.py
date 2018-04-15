#!/usr/bin/python
# -*- coding:utf8 -*-

number = [123,3,3,11,1112,44]
print(number)

# 添加
mix = ['周恒','zhouheng',34,[111,'wwww']]
print(mix)

number.append('赵鸿硕')
print(number)

number.insert(0,'张三')   #对象.insert(第几个，元素)
print(number)

# 访问
print( number[0] )

# 删除
number.remove(123) #对象.remov（obj)   不需要index。书p143
print(number)
del number[1]   #del
print(number)

name1 = number.pop();
print( name1 ) # pop方法。列表是栈，pop：出栈
print(number)

name2 = number.pop(1)
print( name2 ) # pop方法。列表是栈，pop：出栈
print(number)

