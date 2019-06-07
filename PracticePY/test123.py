#!/usr/bin/env python
# -*- coding:utf-8 -*-


file_name = "G:/t\# 空天杯\data\红外图像数据及标签\data1.txt"

data = []

file = open(file_name)
for line in file:

    a = line.strip().split(sep='\t')
    data.append(a)
    print(a)
file.close()
print(data)


# print(data)
# print(type(a))