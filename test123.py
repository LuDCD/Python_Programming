#!/usr/bin/python
# -*- coding:utf8 -*-


# def fact(x): # 求阶乘 factorial.py
#     factorial = 1
#     for i in range(x): # [0,x)
#         factorial = factorial*(i+1)
#     return factorial  # 我是注释
#
# n = int( input('请输入一个数：'))
# print( '%d的阶乘为%d.' % (n, fact(n)) )


###############################N的多次方
# a1 = input()
# list1 = list()
# a = eval(a1)
# if isinstance(a,int):
#     list1.append(1)
# else:list1.append(1.0)
#
# for i in range(1,6):
#   b = list1[i-1]*a
#   list1.append(b)
#   print(list1[i-1], end=' ')
# print(list1[5])


###########################################"温度转换"
# C = ( F - 32 ) / 1.8
# F = C * 1.8 + 32

# inp = input()
# # print(type(inp))
# if inp[0] in ['C','c']:
#     print('F',end='')
#     Ft = eval(inp[1:])*1.8 + 32
#     print("%.2f" % Ft)
# else:
#     print('C',end='')
#     Ct = (eval(inp[1:])- 32 ) / 1.8
#     print("%.2f" % Ct)


#######################################货币转换
inp = input()
# print(type(inp))
if inp[0:3] in ['RMB']:
    print('USD',end='')
    Ft = eval(inp[3:])/6.78
    print("%.2f" % Ft)
else:
    print('RMB',end='')
    Ct = eval(inp[3:])*6.78
    # print("%.2f" % Ct)
    ct1 = '{:.2f}'.format(Ct)
    print(ct1)
