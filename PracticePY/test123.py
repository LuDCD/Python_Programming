#!/usr/bin/python
# -*- coding:utf8 -*-

import requests

r = requests.get('https://www.baidu.com')
print( r.status_code )  # 200 正常