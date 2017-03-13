#!/usr/bin/python
# -*- coding:utf8 -*-

import math
from random import *

def Solving_maze(alist):
    # num = math.ceil( ()/2 )
    num = ( len(alist)+len(alist[0]) )//2

    Set_list = []   # 集合列表，用来存放我的集合

    for i in range(num):
        Set_list.append(set())
    print(Set_list)  # test

    Set_list[0].update({(0,0)})
    Set_list[1].update({(len(alist)-1,len(alist[0])-1)})

    for i in range(2,num):
        x = randint(0,num)
        y = randint(0,num)
        Set_list[i].update({(x,y)})
    print(Set_list) # test


    # for i in range(num):
    #     Set_list[i].append(0)
    # print(Set_list)  # test
    #
    # Set_list[0].append((0,0))
    # Set_list[1].append((len(alist)-1,len(alist[0])-1))
    #
    # for i in range(2,num):
    #     x = randint(0,num)
    #     y = randint(0,num)
    #     Set_list[i].append((x,y))
    # print(Set_list) # test
    #
    #
    # for i in range(num):


# 测试
G = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Solving_maze(G)
# print(G[0][0])