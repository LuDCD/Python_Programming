#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
关于英文字母的操作

@author: ZHOU Heng
"""

def AlphabetList():
    '''
    :return:大写26字母列表
    '''
    # Aord = ord( 'a' )
    # return [chr(i+Aord) for i in range(26)]

    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def alphabetList():
    '''
    :return:返回小写字母表
    '''
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def isLowletters( x ):
    '''
    判断是否为小写字母
    :type x: str
    :rtype:bool
    '''
    flag = 0
    if 'a' <= x <= 'z':
        flag = 1

    return bool( flag )

def ispperletters( x ):
    '''
    判断是否为大写字母
    :type x: str
    :rtype:bool
    '''
    flag = 0
    if 'A' <= x <= 'Z':
        flag = 1

    return bool( flag )

def isLetters( x ):
    '''
    是否为字母
    :type x: str
    :rtype: bool
    '''
    flag = 0
    if 'a' <= x <= 'Z':
        flag = 1

    return bool( flag )

def test():
    A = AlphabetList()
    print( A )


if __name__ == "__main__":
    test()


