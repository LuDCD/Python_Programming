#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
File function

@author: ZHOU Heng
"""

import requests

# 爬取亚马逊的一个商品信息
url1 = 'https://www.amazon.cn/gp/product/B06VXL4CZN/'
kev = { ''}
try:
    r1 = requests.get(url1, header = kev)
except:
    pass

def test():
    pass


if __name__ == "__main__":
    test()



