#!/usr/bin/python
# -*- coding:utf8 -*-

# quick sort
# def QuickSort(list = []):
#     pass

def quickSort(L, low, high):
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

    return L

list = [32,12,5,9,13,1,45,32,17,23,56,21,12]
print(list)
# print(len(list))
quickSort(list,0,len(list)-1)
print(list)