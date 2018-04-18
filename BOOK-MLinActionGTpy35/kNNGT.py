#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
第二章 k-近邻算法再现代码

@author: ZHOU Heng
"""

import numpy as np
import operator

def creatDataSet():
    group = np.array( [ [1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1] ] )
    labels = [ 'A', 'A', 'B', 'B']

    return group, labels

group, labels = creatDataSet()
# print( group.shape, type(group.shape) )       # group.shape = (4, 2)




