#!/usr/bin/env python
# -*- coding:utf-8 -*-


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


# k-近邻算法
def classify0( X, dataSet, labels, k ):
    '''
    :type X:行向量（ 1*n ）
    :type dataSet:矩阵（ m*n ），和 X 列数相同
    :param labels:列向量（m*1）的转置，和 dataSet 的行数相同
    :param k:前 k 个最近的点
    :return:前 k 个中出现频率最高的 label
    '''

    # 获得 dataSet 的行数，即 dataSet 的规模，每一行是包含多个特征的实例.
    dataSetSize = dataSet.shape[0]

    # 产生一个和dataSet相同行、列数的测试数据dataX，
    # 按这样方法复制 np.tile( A, (Y, X) )
    # np.tile( A, (y, x) )：A先沿Y轴(竖着)复制 y 份，再沿X轴(横着)复制 x 份
    dataX = np.tile( X, (dataSetSize, 1) )

    # 算欧式距离
    diffMat = dataX - dataSet   # 求差
    sqDiffMat = diffMat**2
    sumSqDiffMat = sqDiffMat.sum( axis = 1 )        # 在 1轴（X轴）上进行求和
    distances = sumSqDiffMat**0.5
    # print( distances )


    # 排序，得到前 k 名
    distIndexSorted = distances.argsort()   # 默认从小到大


    # 统计前 k 个都是那些类别（标签）
    labFreqTopDistK = {}    # 前 K 个最近距离的实例的标签频率
    for i in range( k ):
        lab = labels[ distIndexSorted[i] ]
        labFreqTopDistK[lab] = labFreqTopDistK.get(lab, 0) + 1


    # 对标签频率进行排序
    labFreq = list( labFreqTopDistK.items() )           # type: list[tuple]
    labFreq.sort( key=lambda x : x[1] ,reverse = True)  # 参数 key 是比较列表元素的什么属性
    # print( labFreq )        # [ ('B', 2), ('A', 1) ]


    return labFreq[0][0]


def file2matrix( filename ):
    '''
    处理文本文件。每行有4个元素，3个特征 + 一个标签
    :type filename:str
    :return:训练样本矩阵 和 类标签向量
    '''
    with open( filename ) as f:
        # 读取文本文件的每一行数据，返回一个 一行作为一个元素 的列表
        listOfLines  = f.readlines()

    numberOfLine = len( listOfLines )
    reMatrix = np.zeros( (numberOfLine, 3) )        # 训练样本矩阵
    labelVector = []       # 类标签向量

    # 遍历 行元素 列表的每一元素
    for i in range( numberOfLine ):
        line = listOfLines[i]
        line = line.strip()         # 除掉收尾空白字符
        tlist = line.split('\t')    # 以水平制表符来切分字符串，返回切分后的元素列表
        reMatrix[i:] = tlist[0:3]
        labelVector.append( tlist[-1] )

    return reMatrix, labelVector





def test():
    group, labels = creatDataSet()
    print( classify0( [0, 0], group, labels, 3))

    # 获得约会数据
    datingDataMat, datingLabels = file2matrix( 'datingTestSet2.txt' )
    # print( datingDataMat, datingLabels)

if __name__ == '__main__':
    test()