#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
File function

@author: ZHOU Heng
"""

def myfind(x,L):
    '''
    寻找到元素 x 在序列 L 中的所有索引，返回缩影列表。
    :param x: int or str
    :param L: list[·] or str
    :return:list[int]
    '''
    return [ a for a in range(len(L)) if L[a] == x ]

def test():
    pass


if __name__ == "__main__":
    test()


