#!/usr/bin/python
# -*- coding:utf8 -*-

# 字典
num = {}
print( type(num) )

# 集合
num2 = {1,2,3,4,5}
# dict1 = { 1:'one', 2:'two', 3:'three'}  这是字典
print( type(num2) )

# 使用set()工厂函数
set1 = set( [2,1,2,3,4,4,5,6,7,7,7,7] )     #set() 改变了顺序
print( set1 )
set2 = set( (7,1,2,3,4,5,5,5,5,6,7,8) )
print( set2 )

# 题目一：去掉列表aList中的重复元素. aList = [1,2,4,5,3,2,6,7,2,3,8,9,16,5]
aList = [1,2,4,5,3,2,6,7,2,3,8,9,16,5]
aList = list( set(aList) )  # set(aList)自动排序了。如果我们关注列表的顺序，则不能使用set()方法
print( aList )

# frozenset()方法
t = frozenset( ['b', 'e', 'r'] )    # 不可变集合（不能增删改）
print( type(t) )

setA = set('Hello, World!')
setB = set('Hello, Python!')
print(setA - setB)
print(setA ^ setB)
