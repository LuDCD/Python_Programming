#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
再现第三章 决策树 算法

@author: ZHOU Heng
"""

import math

# 计算数据的 平均信息熵
def calcShannonEntAvg( dataSet ):
    '''
    :typer dataSet: List[List[·]]
    :return: 标签的平均信息熵
    '''
    l = len( dataSet )      # 数据的总个数

    labelsDict = dict()     # 每个标签出现的次数
    # 遍历数据
    for aData in dataSet:
        key = aData[-1]
        if key in labelsDict.keys():
            labelsDict[key] += 1
        else:
            labelsDict[key] = 1

    shannonEntAvg = 0
    for k in labelsDict:
        p = labelsDict[k]/l
        shannonEntAvg -= p * math.log(p, 2)

    return shannonEntAvg


# 创建测试数
def creatDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]

    labels = ['no surfacing', 'flippers']

    return dataSet, labels



def test():
    dataSet, labels = creatDataSet()
    shannEntAverage = calcShannonEntAvg(dataSet)
    print( shannEntAverage )




if __name__ == "__main__":
    test()