#!/usr/bin/python
# -*- coding:utf8 -*-

import time

def fact1(x):	# 求阶乘 factorial.py
    factorial = 1
    for i in range(x):	# [0,x)
        factorial = factorial*(i+1)
    return factorial		# 我是注释

def fact2(n):
    if n == 1:
        return 1
    else:
        return n * fact2( n-1 )

def test():
    n = 100*100

    t1 = time.time()
    for i in range( n ):
        fact1(100)
    t2 = time.time()
    tt1 = ( t2 - t1 )/n

    t3 = time.time()
    for i in range( n ):
        fact2(100)
    t4 = time.time()
    tt2 = ( t4 - t3 )/n

    print("非递归调用时间{}".format( tt1 ))
    print("递归调用时间{}".format( tt2 ))


# 当该函数作为主函数运行时，才会调用test()方法。
# 当该函数作为一个模块被调用时，则不会调用test()方法。
if __name__ == '__main__':
    test()