#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pandas as pd

# 目录含有中文，使用 engine='python'
data = pd.read_csv("G:/t\# 空天杯\data\红外图像数据及标签\data1.txt", sep="\t", engine='python')
# print(data)
print(data[1,:])

# plt.scatter(data[:,0],data[:,1])
# plt.show()