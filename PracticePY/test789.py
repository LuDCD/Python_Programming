#!/usr/bin/env python
# -*- coding:utf8 -*-

# import sklearn
#
# print( sklearn.__version__ )
#
# testNum = 10
# print( testNum)
# for i in range(0,testNum):
#     print(i)
#
#
#
# a = [1,2,3,4]
# b = a
# a[0] = 2
# print("a:{}\nb:{}".format(a,b))

# from skimage import io
# import matplotlib.pyplot as plt
#
# img = io.imread("./053cat_500_600.jpg")
# io.imshow(img)
# plt.show()
<<<<<<< HEAD
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
df= pd.read_csv('Train.csv')
#df.head()
a = df.describe()
print(df.describe())
=======

import tensorflow.contrib.slim as slim
>>>>>>> 73a2d5b2e766de1473c47361aae1a0bbd204ae0b
