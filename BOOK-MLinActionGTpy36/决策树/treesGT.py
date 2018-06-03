#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
再现第三章 决策树 算法

@author: ZHOU Heng
"""

import math
import numpy as np

# 计算数据集的 平均信息熵
def calcShannonEntAvg(dataSet):
    """
    :typer dataSet: List[List[·]]
    :return: 标签的平均信息熵
    """
    lm = len(dataSet)  # 数据的总个数

    labelsDict = dict()  # 每个标签出现的次数
    # 遍历数据
    for aData in dataSet:
        key = aData[-1]
        if key in labelsDict.keys():
            labelsDict[key] += 1
        else:
            labelsDict[key] = 1

    shannonEntAvg = 0
    for k in labelsDict:
        p = labelsDict[k] / lm
        shannonEntAvg -= p * math.log(p, 2)

    return shannonEntAvg


# 创建测试数
def creatDataSet():
    dataSet = [[1, 1, "mayve"], [1, 1, "yes"], [1, 0, "no"], [0, 1, "no"], [0, 1, "no"]]

    labels = ["no surfacing", "flippers"]

    return dataSet, labels


# 按照给定特征及其特征值拆分数据集
def splitDataSet(dataSet, axis, values):
    """
    :type dataSet: List[List[·]]
    :param axis: 给定的特征
    :param values: 给定的特征的值
    :return:拆分后的数据集
    """
    reData = []
    for aData in dataSet:
        if aData[axis] == values:
            reData.append(aData[:axis] + aData[axis + 1 :])

    return reData


# 选择最好的数据集划分方式
def chooseBestFeatureToSplite(dataSet):
    """
    :type dataSet: List[List[·]]
    :return: 划分最好的那个特征
    """
    # print( dataSet )

    # 把 dataSet 矩阵化
    npDataSet = np.array(dataSet)

    numFeatures = npDataSet.shape[1] - 1    # 特征的个数
    numData = npDataSet.shape[0]            # 数据集中实例的个数

    baseShannonEnt = calcShannonEntAvg(dataSet)
    bestFeatureIndex = -1   # 最好分类特征
    maxInfGain = 0          # 最大信息增益
    # 遍历所有特征
    for i in range(numFeatures):
        # 第 i 个特征的所有值
        featureValues = set(npDataSet[:, i])
        print(featureValues)

        shannEntSplited = 0
        for value in featureValues:
            # value = eval( valueStr )
            splitedData = splitDataSet(dataSet, i, value)
            p = len(splitedData) / numData
            shannEntSplited += p * calcShannonEntAvg(splitedData)

        # 计算信息增益
        # infGain = shannEntSplited - baseShannonEnt  # 错了！！
        infGain = baseShannonEnt - shannEntSplited

        if infGain > maxInfGain:
            maxInfGain = infGain
            bestFeatureIndex = i

    return bestFeatureIndex


# 多数表决
def majorityCnt(classList):
    classDict = dict()
    for vote in classList:
        if vote not in classDict:
            classDict[vote] = 0
        else:
            classDict[vote] += 1

    sortedClassDict = sorted(classDict.items(), key=lambda x:x[0], reverse=True)

    return sortedClassDict[0][0]



def test():
    dataSet, labels = creatDataSet()
    shannEntAverage = calcShannonEntAvg(dataSet)
    # print( shannEntAverage )

    # 拆分数据
    # print( splitDataSet(dataSet, 0, 0) )

    # 最好的分组特征
    bestFeature = chooseBestFeatureToSplite(dataSet)
    print(bestFeature)

    # 测试表决器
    # print(majorityCnt([1,2,2,2]))


if __name__ == "__main__":
    test()
