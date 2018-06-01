#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
File function

@author: ZHOU Heng
"""

import numpy as np

a = np.arange(1, 200)
n_max = int(len(a) ** 0.5)
is_prime = np.ones( len(a), dtype=bool)
print(a)
print( is_prime )
is_prime[0] = False
# print( a[is_prime] )
for i in range(2, n_max):
    if i in a[is_prime]:
        is_prime[(i ** 2 - 1) :: i] = False

print(a[is_prime])
print( a[is_prime].shape )

