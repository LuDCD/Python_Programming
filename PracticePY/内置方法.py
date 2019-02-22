#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
File function

@author: ZHOU Heng
"""


# =============== filter(function, iterable)
# 用function来过滤可迭代对象
res = filter(lambda n:n>5, range(10))
print("转为list：{}".format(list(res)))


# =============== map(func, iterable)
# 可迭代对象的元素都用func处理一遍
res_map = map(lambda x:x**2, range(10))
# 等价于
res_list = [i**2 for i in range(10)]
print("res_list:{}".format(res_list))
print(list(res_map))

# =============== frozenset() 冻结集合，使之不可修改
print("\n\nfrozenset()方法")
aSet = set(range(10))
frozSet = frozenset(aSet)
aSet.pop()
try:
    frozSet.pop() # AttributeError: 'frozenset' object has no attribute 'pop'
except AttributeError as e:
    print("捕获的异常为：{}".format(e))
alist = list(aSet)
frozList = frozenset(alist)
alist.pop()
# frozList.pop() # AttributeError: 'frozenset' object has no attribute 'pop'


# =============== round(number, ndigits:int)
print("\n\nround()方法")
print(round(10.25534, 2))