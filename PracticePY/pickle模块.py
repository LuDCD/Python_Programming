#!/usr/bin/python
# -*- coding:utf8 -*-


import pickle

# 存放 pickling
# 读取 unpickling

# =====================【例1】
print("【例1】")
my_list = [123,3.14,'周恒',(456,'我是元组'),[789,'我是列表中的列表的元素']]
with open('pickle_list.pkl', 'wb') as pickle_file: # pickle_file文件句柄
    # 腌制
    # pickle.dump( my_list, pickle_file ) # dump()使用方法（推荐）
    pickle_file.write(pickle.dumps(my_list)) # dumps()使用方法


with open('pickle_list.pkl', 'rb') as pickle_file:
    # 载入
    my_list2 = pickle.load( pickle_file ) # 推荐
    print( "my_list:\n{}".format(my_list2) )






