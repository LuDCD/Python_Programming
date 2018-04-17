#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
使用txt【保存】和【读取】【列表变量】

@author: ZHOU Heng
"""

def text_save(content, filename, mode='a'):
    # Try to save a list variable in txt file.
    '''
    :param content:列表变量
    :param filename:文件名，如'1.txt'
    :param mode:读写方式，默认mode = 'a'
    :return:在当前目录下创建一个名为filename文件，并且将列表的每个元素逐一写入文件（加入换行符）
    '''
    file = open(filename,mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

def text_read( filename ):
    # Try to read a txt file and return a list.Return [] if there was a mistake.
    '''
    :param filename: 文件名，如'1.txt'
    :return:函数返回一个列表,里面包含每行的内容，并且自动屏蔽换行符(如果没有找到该文件名，返回空列表:[])
    '''
    try:
        file = open(filename,'r')
    except IOError:
        # print(IOError)
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]     # 每一个元素都是字符串
        # content[i] = eval( content[i][:len(content[i])-1] )     # 如果文件里面存的是数字列表可用这个

    file.close()
    return content



def test():
    pass


if __name__ == "__main__":
    test()
