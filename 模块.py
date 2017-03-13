#!/usr/bin/python
# -*- coding:utf8 -*-

'''
① import 模块名
② from 模块名 import 函数名
③ import 模块名 as 新名字
'''

import factorial
print( factorial.fact(5))
print( factorial.__name__ )

from factorial import fact
print( fact(5) )

import factorial as fa
print( fa.fact(5))

print( __name__ )


# 搜索路径
import sys
print( sys.path )   # 是个列表
# 最佳的路径：'D:\\Program Files (x86)\\Python35-32\\lib\\site-packages

# 添加路径
# sys.path.append('路径')

# 包（package）
# 创建方法
# 1、创建一个文件夹，用于存放相关的模块，文件夹的名字即为包的名字；
# 2、在文件夹中创建一个__init__.py的模块文件，内容可以为空
# 3、将相关的模块放在文件夹中

# 调用
# 包.模块名






