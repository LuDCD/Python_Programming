#!/usr/bin/python
# -*- coding:utf8 -*-


# lambda表达式
# lambda 输入参数:返回的结果（一个运算表达式）
# （就是说：冒号前面表示的是输入，这个输入经过冒号后面的表达式运算之后返回）

# 一般函数
def add(x,y):
    return x+y

print( add(3,4) )

# 使用lambda构造匿名函数
g = lambda x,y : x+y
print( g(4,5) )


#可通过help(filter)来获得帮助

# filter() 过滤器
# filter(function or None, iterable) --> filter object
# Return an iterator yielding those items of iterable for which function(item) is true.
# If function is None, return the items that are true.

print( list(filter(None,[1,0,True,False])))

def odd(x):
    return x % 2
temp = range(10)
print( filter(odd,temp) )   # 这里只要传入函数的名字，即odd就可以了。不要传odd()
print( list(filter(odd,temp)) )

# odd()函数可以换一种写法
show = filter( lambda x : x%2, range(10) )
print( list(show) )


# map()
# map(func, *iterables) --> map object

show2 = map( lambda x : x*2, range(10) )
print( list(show2) )