#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
File function

@author: ZHOU Heng
"""

import requests

################## 爬取亚马逊的一个商品信息
url1 = 'https://www.amazon.cn/gp/product/B06VXL4CZN/'
kev = { 'user-agent' : 'Mozilla/5.0' }
try:
    r1 = requests.get(url1, headers = kev, timeout=30)
    r1.raise_for_status()    # 如果状态码不是200，引发HTTPError异常
    # r.encoding = r.apparent_encoding
    # print( r.apparent_encoding )        # Windows-1254
    r1.encoding = 'utf-8'
    print( len(r1.text) )
    print( type(r1.text) )       # <class 'str'>
except :
    print('产生异常')


######################### 百度搜索关键词提交
'''例如：查询西安。https://www.baidu.com/s?wd=西安
http://www.baidu.com/s?wd=keyword
'''

kv = {'wd' : 'Python'}
r2 = requests.get( 'https://www.baidu.com/s', params=kv )
print( r2.request.url )
print( r2.status_code )
print( len( r2.text ) )

if __name__ == "__main__":
    pass
