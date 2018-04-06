#!/usr/bin/env python
# -*- coding:utf8 -*-

import time
import random

n = 1000*1000*10

strtime = time.time()
pn = 0

# 版本一 大概 15s 左右
# for i in range(n):
#     x, y = random.random(), random.random()
#     if pow( x**2+y**2, 0.5 ) < 1:
#         pn = pn + 1

# 版本二 运行大概 12s 左右
# for i in range(n):
#     x, y = random.random(), random.random()
#     if x+y<1:
#         pn = pn + 1
#     elif pow( x**2+y**2, 0.5 ) < 1:
#         pn = pn + 1

# 版本三 10s 左右
for i in range(n):
    x, y = random.random(), random.random()
    if x +y > 2**0.5:
        continue
    elif x+y<1:
        pn = pn + 1
    elif pow( x**2+y**2, 0.5 ) < 1:
        pn = pn + 1

pi = 4 * pn/n

endtime = time.time()
print( "耗时{:.5f}s".format(endtime-strtime) )
print("pi = {}".format(pi))