#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
和pickle模块一起看

json多语言通用
pickle仅python使用

@author: ZHOU Heng
"""

import json


# 【例1】
print("【例1】:")
info = {
    "name":"hzhou",
    "age":23
}

# 写入文件
with open("json.jn", "w+") as f:
    f.write(json.dumps(info)) # dumps()方法

# 读入
with open("json.jn", "r") as f: # f:文件句柄
    # info_read = json.loads(f.read()) # loads()方法
    # load()方法（推荐）
    info_read = json.load(f)
    print("age:{}".format(info_read["age"]), "\ntype(info_read):{}".format(type(info_read)))



