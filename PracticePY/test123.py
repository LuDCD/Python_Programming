#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")
# print(len(data))

plt.scatter(data[:,0],data[:,1])
plt.show()