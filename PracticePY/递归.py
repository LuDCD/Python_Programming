#!/usr/bin/python
# -*- coding:utf8 -*-


# 递归实现x!
def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)

n = 5
print( '%d! = %d' % (n, fact(n)) )

# 非递归
def fact2(x):
    factorial = 1
    for i in range(x):
        factorial = factorial*(i+1)
    return factorial
n = int( input('请输入一个数：'))
print( '%d的阶乘为%d.' % (n, fact2(n)) )


# 斐波那契数列
# 递归实现
def F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-1)+F(n-2)    # 分治思想

print( F(20) )      # 当 n = 35 时，速度明显降低

# 迭代实现
# 实现一
def F1( n ):
    t = [1,1]
    for i in range(2,n):    # range(m,n)    <=>     [m,n)
        t.insert( i,t[i-2]+t[i-1] )
    return t[n-1]

# 实现二
def F12( n ):
    n1 = 1
    n2 = 1
    if n < 1:
        print('输入有误！')
        return -1
    while ( n-2 ) > 0:
        n3 = n1 +n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3

print( F1(20) )
print( F12(20) )
