#!/usr/bin/env python
# -*- coding:utf8 -*-

###########################################"货币转换"
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