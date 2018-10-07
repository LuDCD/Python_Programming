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

from skimage import io
import matplotlib.pyplot as plt

img = io.imread("./053cat_500_600.jpg")
io.imshow(img)
plt.show()
