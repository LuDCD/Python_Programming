#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
第二章 k-近邻算法再现代码

@author: ZHOU Heng
"""

import numpy as np
import os

import matplotlib
import matplotlib.pyplot as plt


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


# 从文件中读出数据，并处理返回
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
        tlist = line.split('\t')    # 以水平制表符来切分字符串，返回切分后的字符元素列表
        reMatrix[i, :] = tlist[0:3]
        labelVector.append( tlist[-1] )
        # 这里没有进行 int( tlist[-1] )强转为数字，得到的字符串。根据需要自己转数字。

    return reMatrix, labelVector


def drawData( x, y , labels):
    '''
    :param x: x轴数据
    :param y: y轴数据
    :param labels: 分类标签数据
    :return:
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter( x, y, s=15.0*np.array(labels), c=15.0*np.array(labels) )    # size, color

    plt.show()


# 归一化数据
def autoNorm( dataSet ):
    minValues = dataSet.min(0)      # 列（0轴）最小值向量。
    maxValues = dataSet.max(0)

    # 造坑
    normDataSet = np.zeros( dataSet.shape )

    # 归一化，把数填上
    normDataSet = dataSet - np.tile( minValues, ( dataSet.shape[0], 1) )
    minMaxDif = np.tile( maxValues - minValues, ( dataSet.shape[0], 1) )
    normDataSet = normDataSet / minMaxDif

    # 返回归一化数据。最大，最小值会在以后归一化测试数据时用到
    return normDataSet, maxValues, minValues
    # print( normDataSet )

# 分类器测试
def datingClassTest():
    dataTestRatio = 0.1     # 选 10% 的数据，来测试

    datingDataSet, labelsVectors = file2matrix( 'datingTestSet.txt' )    # 获得数据
    datingDataSet, maxValues, minValues = autoNorm( datingDataSet )       # 数据归一化

    m = datingDataSet.shape[0]

    orrorNum = 0
    # 选前 10%(=dataRatio*m) 作为测试
    numTestData = int( m*dataTestRatio )    # 必须整数化，因为后面有索引
    trainData = datingDataSet[numTestData:m, :]
    trainLabels = labelsVectors[numTestData:m]
    for i in range( numTestData ):
        lab = classify0(datingDataSet[i, :], trainData, trainLabels, 3)
        if lab != labelsVectors[i]:
            orrorNum += 1

    return orrorNum / float(numTestData)


# 把图像数据转换成向量
def img2vector( filename ):
    '''
    :type filename: 图像数据(已知为：32*32 矩阵)文件名字符串 '0_1.txt'
    :return:向量
    '''
    reVector = np.zeros( (1, 32*32) )

    with open(filename) as fp:
        for i in range( 32 ):
            strNum = fp.readline()
            for j in range(32):
                reVector[0, 32*i+j] = eval( strNum[j] )

    return reVector


# 手写数字识别系统
def handwritingClassTest():
    fileNameList = os.listdir('trainingDigits')     # 获得这个文件夹下的文件名(如：'9_11.txt')列表
    m = len( fileNameList )     # 有多少个文件
    trainData = np.zeros( (m,32*32) )   # 创建一个m行32*32列的矩阵，用来存放这m个图像数据

    classNumLabels = []
    for i in range(m):
        fileNameStr = fileNameList[i]
        fileStr = fileNameStr.split('.')[0]        # '9_11'
        # 标记是哪个数字
        numLabel = eval( fileStr.split('_')[0] )    # 9
        classNumLabels.append( numLabel )
        # 这个数字的图像数据
        trainData[i,:] = img2vector('trainingDigits/{}.txt'.format(fileStr))

    error = 0
    # 如法炮制，来测试数据
    testFileNameList = os.listdir('testDigits')     # 获得这个文件夹下的文件名(如：'9_11.txt')列表
    tm = len( testFileNameList )
    for i in range(tm):
        fileNameStr2 = testFileNameList[i]
        fileStr2 = fileNameStr2.split('.')[0]   # '0_3'
        num2 = eval( fileStr2.split('_')[0] )   # 0

        # 获得测试图像数据
        X = img2vector('testDigits/{}.txt'.format(fileStr2))
        # 使用 k-近邻算法
        k_NNclassNum = classify0( X, trainData, classNumLabels, 3 )

        # print('数字为{}'.format(num2),'{}是分类结果'.format(k_NNclassNum) )

        # 统计错误数
        if k_NNclassNum != num2:
            error += 1


    print('错误率：{}'.format(error/tm))



def test():
    # group, labels = creatDataSet()
    # print( classify0( [0, 0], group, labels, 3))



    # 获得约会数据
    datingDataMat, datingLabels = file2matrix( 'datingTestSet2.txt' )
    for i in range( len(datingLabels) ):
        datingLabels[i] = eval( datingLabels[i] )

    # 我知道 datingTestSet2.txt 里面的数据的label 是数字，
    # 由于file2matrix,转换之后的全是字符，所以我们要变数字字符为数字，因为后面用到数字的值
    # print( datingDataMat, datingLabels)



    # 可视化
    drawData( datingDataMat[:,0], datingDataMat[:,1], datingLabels)



    # 归一化数据
    # normDatingMat, maxVector, minVector = autoNorm( datingDataMat )



    # 查看错误率
    # orrorRatio = datingClassTest()
    # print( orrorRatio )



    # 图像数据转换为向量
    # numVector = img2vector('testDigits/0_13.txt')
    # print( numVector )
    # print( type(numVector) )



    # 手写测试系统
    # handwritingClassTest()



if __name__ == '__main__':
    test()