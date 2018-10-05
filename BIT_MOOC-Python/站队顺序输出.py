#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
有一群人站队，每人通过一对整数(h, k)来描述，其中h表示人的高度，k表示在此人前面队列中身高不小于此人的总人数。

实现一个算法输出这个队列的正确顺序。

输入格式为二维列表，即 list[list[]]形式
外层list包含队列中全部的人，内层list为[h,k]格式，代表个人信息。

输出格式为：list[list[int]]形式

与输入格式一样，需要按照队列顺序排列。

输入输出示例
输入	输出
示例 1
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


@author: ZHOU Heng
"""

class Solution:
    def mtsort(self):
        n = eval(input())
        fa = [0]
        while fa[-1] < n:
            if len(fa) == 1:
                fa.append(1)
            else:
                fa.append(fa[-1] + fa[-2])

        s = sum(fa)
        l = len(fa)
        avg = int(s/l)
        fa.append(s)
        fa.append(avg)

        for i in range(l+2):
            if i == 0:
                print(fa[i], end=',')
            elif i == l+2-1:
                print('', fa[i])
            else:
                print('', fa[i], end=',')


def main():
    sol = Solution()
    sol.fab()


if __name__ == "__main__":
    main()