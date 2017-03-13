#!/usr/bin/python
# -*- coding:utf8 -*-

def fact(x):	# 求阶乘 factorial.py
    factorial = 1
    for i in range(x):	# [0,x)
        factorial = factorial*(i+1)
    return factorial		# 我是注释

def test():
    print('10的阶乘为%d.' % fact(10) )
    print('5的阶乘为%d.' % fact(5) )

# 当该函数作为主函数运行时，才会调用test()方法。
# 当该函数作为一个模块被调用时，则不会调用test()方法。
if __name__ == '__main__':
    test()