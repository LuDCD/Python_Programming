#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
测试 requests 库是否正常安装

@author: ZHOU Heng
"""

import requests

r = requests.get('https://www.baidu.com')
print( r.status_code )      # 200 正常


