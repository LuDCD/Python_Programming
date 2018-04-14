#!/usr/bin/env python
# -*- coding:utf8 -*-

import math

def isPrime(num):
    ' 判断一个数是否为素数 '
    flag = 0
    if num in [2, 3, 5]:
        flag = 1
    else:
        for i in range(2, int( math.sqrt(num)+1 ) ):
            flag = 1
            if num % i == 0:
                flag = 0
                break

    # if flag == 1:
    #     return True
    # else:
    #     return False

    return bool( flag )     # 简介写法

# 1.保存入txt文件
# 输入：content(列表变量)，filename(文件名，如'1.txt'),mode(读写方式，默认mode = 'a').
# 输出：在当前目录下创建一个名为filename文件，并且将列表的每个元素逐一写入文件（加入换行符）.

def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename,mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

# 2.读取出txt文件
# 输入：filename(文件名，如'1.txt').
# 输出：函数返回一个列表,里面包含每行的内容，并且自动屏蔽换行符(如果没有找到该文件名，返回空列表).

def text_read(filename):
    # Try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        content[i] = eval( content[i][:len(content[i])-1] )

    file.close()
    return content

n = 10*1000
primeList = []
for i in range( n ):
    if isPrime(i):
        primeList.append(i)
# text_save( primeList, 'test123.txt', 'w')
s = text_read('test123.txt')

print(primeList)
print( s )
# print( len( primeList) )