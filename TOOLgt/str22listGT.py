#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
['a', '2', 'c', '1', 'e']和
'a2c1e'之间的相互转换

@author: ZHOU Heng
"""

def str2list( string ):
    '''
    字符串转列表
    :type string: str
    :return:list
    '''
    return list( string )

def list2str( List ):
    '''
    列表转字符串
    :type List: list[str]
    :return:str
    '''
    return ''.join( List )


def test():
    aList = ['a', '2', 'c', '1', 'e']
    s = 'up3ist'
    s2 = list2str(aList)
    print( type(s2), s2 )
    sList = str2list(s)
    print( type(sList), sList )


if __name__ == "__main__":
    test()


