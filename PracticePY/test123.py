#!/usr/bin/python
# -*- coding:utf8 -*-

# import numpy as np
# a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# print( a.shape )
# print(a[[2]].sum())

for i in range(5):
    i += 1
    print(i)

a = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
print(sum(a))


def openNum(self, gird, r, c):
    openN = 0

    # 上下左右
    up = gird[r-1][c]
    down = gird[r+1][c]
    rig = gird[r][c+1]
    lef = gird[r][c-1]

    if r != 0 and c != 0:
        openN = sum( up, down, rig, lef )
    elif r == 0 and c != 0:
        openN = sum( down,rig, lef )
    elif r != 0 and c == 0:
        openN = sum( up, down, rig)
    else:
        openN = sum( )