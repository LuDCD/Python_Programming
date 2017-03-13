#!/usr/bin/python
# -*- coding:utf8 -*-

# 字典，Python唯一的映射类型
# 标志花括号 {}

dict1 = { 1:'one', 2:'two', 3:'three'}
print('dict1:',dict1)
print('1的英文为：',dict1[1])

# 工厂函数dict()
dict2 = dict( (('China','五星红旗'), ('American','星条旗'), ('Britain','米字旗')) )
# 这里传进dict()的是元组，也可以是列表
print( dict2 )

dict3 = dict( [('China','五星红旗'), ('American','星条旗'), ('Britain','米字旗')] )
print( dict3 )


# 可以对键进行赋值，改变他们对应的关系。如果键不存在就会自动创建这个键（这一点与序列不同）
dict1[1] = 'One'
print( 'dict1:', dict1 )
dict1[4] = 'Four'
print( 'dict1:', dict1 )

# 关键字来创建字典
dict4 = dict( 小甲鱼 = '让编程改变世界', 毛主席 = '好好学习', Nick = 'Impossible is nothing' )
# 它的顺序会自己调整。
# 并且 key 不能加引号↓
# '小甲鱼' = '让编程改变世界'
# SyntaxError: keyword can't be an expression.
print( dict4 )

# 工厂函数：dict(),str(),list(),tuple()


