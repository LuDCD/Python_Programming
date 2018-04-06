#!/usr/bin/env python
# -*- coding:utf8 -*-

# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

n = eval( input() )

i = 2

while n != 1:
    while n % i== 0:
        n //= i
        if n==1:
            print('{:d}'.format(i))

        else:
            print('{:d} *'.format(i),end=' ')

    i += 1