#!/usr/bin/python
# -*- coding:utf8 -*-

# 2016.11.5

# 冒泡排序，升序
def BubbleSort(list = []):

    length = len(list)
    for i in range(length):
        for j in range(i+1,length):     # [i+1,length)
            # 每次拿 list[j] 和 list[i] 比，如果list[i]比list[j]大，则交换。
            # e.g.第一次：list[1]依次和[2:length]比较，一轮完了，list[1]变成最小的了
            if list[i] > list[j]:
                t = list[i]
                list[i] = list[j]
                list[j] = t

list1 = [2,4,8,1,4,78,21,4]
print(list1)
BubbleSort(list1)
print(list1)

