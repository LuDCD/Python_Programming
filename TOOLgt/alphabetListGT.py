#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
字母表列表

@author: ZHOU Heng
"""

def AlphabetList():
    # Aord = ord( 'a' )
    # return [chr(i+Aord) for i in range(26)]

    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def alphabetList():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def test():
    A = AlphabetList()
    print( A )


if __name__ == "__main__":
    test()


