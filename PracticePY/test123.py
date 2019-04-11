#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request

for i in range(1,10):
    key=urllib.request.quote(i+"是什么")
    url="http://www.baidu.com/s?wd="+key
    req=urllib.request.Request(url)
    data=urllib.request.urlopen(req).read()
    fh=open("F:/python/代码/baidu"+str(i)+"是什么.html","wb")
    fh.write(data)
    fh.close()
    print("F:/python/代码/baidu"+str(i)+"是什么.html")

