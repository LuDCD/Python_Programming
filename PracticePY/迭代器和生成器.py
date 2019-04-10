#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
File function

@author: ZHOU Heng
"""

# 1 ================ 列表生成式
alist = [i for i in range(10)]
print(alist, type(alist))

# 2 ================  生成器
# 列表，访问前就存在于内存里。
# 生成器，不访问前内存里不存在。只有在调用时才会生成相应的数据
#         只记住当前位置
#         只有__nex__()方法，generator.__next__()

# 【例1】
print("生成器【例1】：")
agen = (i * 2 - 5 for i in range(10))
print(agen)
for e in agen:
    print(e)

# 【例2】
print("生成器【例2】:")


def fabi():
    a, b = 0, 1  # 表示第cnt个斐波那契数列的数
    while True:
        yield b
        a, b = b, a + b


f = fabi()
print(f)  # <generator object fabi at 0x000001C0980DF728>
for i in f:
    print(i)
    if i > 100:
        break
