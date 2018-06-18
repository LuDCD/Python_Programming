#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
用 300 个符合正态分布的点 X[x0 , x1 ]作为数据集，
根据点 X[x0 , x1 ]计算生成标注 Y_，将数据集标注为红色点和蓝色点。
标注规则为：当 x0^2 + x1^2 < 2 时，y_=1，标注为红色；
当 x0^2 + x1^2 ≥ 2 时，y_=0，标注为蓝色。

我们分别用无正则化和有正则化两种方法，拟合曲线，把红色点和蓝色点分开。
在实际分类时，
如果前向传播输出的预测值 y 接近 1 则为红色点概率越大，
接近 0 则为蓝色点概率越大，

输出的预测值 y 为 0.5 是红蓝点概率分界线。

@author: ZHOU Heng
"""
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# 0 产生模拟数据集
SEED = 2
rng = np.random.RandomState(seed=SEED)

# 产生300组坐标点(x0, x1)作为输入
DATA_SIZE = 300
X = rng.randn(DATA_SIZE, 2)

# 如果两坐标的平法和小于2，则 Y 赋值为 1 ；否则赋值为0
Y_ = [int(e[0] ** 2 + e[1] ** 2 < 2) for e in X]
# 把 Y_ 转化为 向量 ndarry
Y_vr = np.array(Y_)     # 行向量
Y_vc = Y_vr.reshape(-1, 1)      # 列向量
print(X)
print(Y_vr)
# 绘图

plt.scatter(X[:, 0], X[:, 1], s=5.0 * Y_vr + 15.0, c=15.0 * Y_vr + 15.0)
plt.show()