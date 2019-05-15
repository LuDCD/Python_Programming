#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
File function

@author: ZHOU Heng
"""
import torch as th
from matplotlib import pyplot as plt
import numpy as np
from IPython import display

# 设置随机种子
th.manual_seed(seed=1000)


def get_fake_data(batch_size=8, x_end = 20):
    """
    产生随机数据。y = 2x + 3
    :param batch_size:
    :return:
    """
    x = th.rand(batch_size, 1) * x_end  # 把 0-1 之间的值放大到 0-20 之间
    y = x * 2 + (1 + th.rand(batch_size, 1)) * 3

    return x, y


def linear_predictive(x,y):
    """
    线性回归
    :return:
    """
    # 随机初始化参数
    w = th.rand(1,1)
    b = th.zeros(1,1)

    lr = 0.001

    STEPS = 20000
    for i in range(STEPS):

        # forward
        y_ = x.mm(w) + b.expand_as(y)
        loss = 0.5*(y_ - y) ** 2  # 均方误差


        # backward
        dloss = 1
        dy = dloss * (y_-y)
        dw = x.t().mm(dy)
        db = dy.sum()

        # 更新参数
        w.sub_(lr*dw)
        b.sub_(lr*db)

    return w,b


def main():
    x_end = 20
    x,y = get_fake_data(x_end)
    plt.scatter(x.squeeze().numpy(), y.squeeze().numpy())
    # plt.scatter(x, y)  # 和上面效果一样

    w,b = linear_predictive(x,y)
    print(w,b)

    plt.plot([0,x_end], [b,w*x_end+b], 'r')

    plt.show()


if __name__ == "__main__":
    main()