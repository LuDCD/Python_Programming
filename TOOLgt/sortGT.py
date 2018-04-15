#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
File function

@author: ZHOU Heng
"""


def BubbleSort( list = [] ):
    '''
    # 冒泡排序，升序
    :type list: List[int]
    :return:不返回，指针操作。
    '''
    length = len(list)
    for i in range(length):
        for j in range(i+1,length):     # [i+1,length)
            # 每次拿 list[j] 和 list[i] 比，如果list[i]比list[j]大，则交换。
            # e.g.第一次：list[1]依次和[2:length]比较，一轮完了，list[1]变成最小的了
            if list[i] > list[j]:
                t = list[i]
                list[i] = list[j]
                list[j] = t

def quickSort(L, low, high):
    '''
    :param L: List[int]
    :param low: int
    :param high: int
    :return:
    '''
    i = low
    j = high
    if i >= j:
        return L

    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key

    quickSort(L, low, i-1)
    quickSort(L, j+1, high)

def test():
    pass


if __name__ == "__main__":
    test()


