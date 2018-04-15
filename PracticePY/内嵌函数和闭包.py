#!/usr/bin/python
# -*- coding:utf8 -*-


# 内嵌函数，即嵌套定义，在Python里是合法的，这点与C语言不同
def fun1():
    print("fun1正在被调用.....")
    def fun2():                         # 定义fun2
        print('fun2正在被调用....')

    fun2()                              # 调用fun2

fun1()
# 内部函数的整个作用域都在外部函数之内
# 就是说内嵌的函数之内在内部使用，出了作用域则不可调用


# 闭包 closure
# 定义：如果一个内部函数引用了外部作用域的变量，则这个内部函数被认为闭包

def aFun(x):
    def bFun(y):
        return x*y
    return bFun

print(aFun(5))
print('aFun_type:',type(aFun(5)))
print( aFun(5)(8) )

'''
def funX():
    x = 5
    def funY():
        x *= x;             # 报错
        return x
    return funY()

print( funX() )

# UnboundLocalError: local variable 'x' referenced before assignment
'''

# 解决方案一：使用容器类型，因为容器类型存放在栈里面，不会被屏蔽。
def funX():
    x = [5]
    def funY():
        x[0] *= x[0];             # 报错
        return x
    return funY()

print( funX() )


# 解决方案二：可以使用nonlocal关键字
def funM():
    x = 5
    def funN():
        nonlocal x
        x *= x;             # 报错
        return x
    return funN()

print( funM() )

