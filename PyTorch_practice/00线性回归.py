#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
File function

@author: ZHOU Heng
"""
import torch as th
from matplotlib import pyplot as plt
from IPython import display

# 设置随机种子
th.manual_seed(seed=1000)


def get_fake_data(batch_size=8):
    """
    产生随机数据
    :param batch_size:
    :return:
    """
    x = th.rand(batch_size, 1) * 20  # 把 0-1 之间的值放大到 0-20 之间
    y = x * 2 + (1 + th.rand(batch_size, 1)) * 3

    return x, y


def main():
    x,y = get_fake_data()
    plt.scatter(x.squeeze().numpy(), y.squeeze().numpy())
    # plt.scatter(x, y)  # 和上面效果一样
    plt.show()


if __name__ == "__main__":
    main()