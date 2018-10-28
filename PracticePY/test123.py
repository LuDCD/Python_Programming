#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import os
# #
# # def file_name(file_dir):
# #     for root, dirs, files in os.walk(file_dir):
# #         print(root) #当前目录路径
# #         print(dirs) #当前路径下所有子目录
# #         print(files) #当前路径下所有非目录子文件
# #
# # if __name__ == '__main__':
# #     file_dir = os.getcwd()
# #     print(os.listdir(file_dir), file_dir)

<<<<<<< HEAD
import numpy as np

aa = np.array([[1,2,3], [4,5,6], [7,8,9]])
labs = [0, 1, 0]
dic = dict()
labs_set = set(labs)

for la in labs_set:
	for i in range(len(labs)):
		if labs[i] == la:
			if la in dic:
				dic[la] = dic[la] + aa[i]
			else:
				dic[la] = aa[i]

for k in dic:
    dict[k] /= labs.count(int(k))

=======

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件


if __name__ == "__main__":
    file_dir = os.getcwd()
    print(os.listdir(file_dir), file_dir)
>>>>>>> 73a2d5b2e766de1473c47361aae1a0bbd204ae0b
