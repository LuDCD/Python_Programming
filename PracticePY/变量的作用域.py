#!/usr/bin/python
# -*- coding:utf8 -*-

# 类似于C语言的不在赘述。以下介绍不同点
# 1、在函数内访问全局变量，没问题。
#   一旦你想修改全局变量，Python会自动复制一份和全局变量一模一样的变量（名字相同）。
# 2、如何在函数内修改全局变量？
#   global关键字声明就ok了


def test():
    global globals_num      # 这个编译器比较吊，没这句话编译失败
    globals_num += 1
    print(globals_num)

globals_num = 100

test()

print(globals_num)