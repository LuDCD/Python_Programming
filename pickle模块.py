#!/usr/bin/python
# -*- coding:utf8 -*-


import pickle

# 存放 pickling
# 读取 unpickling


my_list = [123,3.14,'周恒',(456,'我是元组'),[789,'我是列表中的列表的元素']]
pickle_file = open('pickle_list.pkl', 'wb')
# 腌制
pickle.dump( my_list, pickle_file )     # dump()在pickle里面
pickle_file.close()

# 载入
pickle_file2 = open('pickle_list.pkl', 'rb')
my_list2 = pickle.load( pickle_file2 )
print( my_list2 )






