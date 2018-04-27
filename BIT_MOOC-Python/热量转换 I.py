#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1卡路里约等于4.186焦耳。

编写程序，对用户输入的热量进行转换，要求如下：

（1）用户输入热量值和热量标签，程序转换后输出热量值和热量标签；

（2）输出热量值保留小数点后3位；

（3）输入输出数据格式为：热量值+热量标签，卡路里标签为cal，焦耳标签为J。

输入输出示例
示例 1
22cal
92.089J

示例 2
2.12345678J
0.507cal

@author: ZHOU Heng
"""

strIn = input()

strOut = ''
if strIn[-1] == 'l':
    # 1卡路里约等于4.186焦耳。
    J = 4.186 * eval(strIn[:-3])
    strOut = '{:.3f}J'.format(J)
else:
    cal = eval(strIn[:-1]) / 4.186
    strOut = '{:.3f}cal'.format(cal)

print(strOut)




