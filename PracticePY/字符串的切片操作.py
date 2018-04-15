# -*- coding:utf8 -*-

# 1、翻转
s = 'abcdefijk'
s = s[::-1]
print(s)

# 2、隔一个取一个
n = '0123456789'
n = n[::2]
print(n)

# 3、面向对象直接取
print( ('zs', 'ls', 'ww')[1] )
# 相当于
# a = ('zs', 'ls', 'ww')
# b = a[1]
# print(b)

