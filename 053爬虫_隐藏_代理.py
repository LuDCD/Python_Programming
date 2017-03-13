#!/usr/bin/python
# -*- coding:utf8 -*-

import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码


'''
隐藏方式一：代理
步骤：
1、参数是一个字典 {'类型':'代理IP:端口号'}
    proxy_support = urllib.request.ProxyHandler({})
2、定制、创建一个opener
    opener = urllib.request.build_opener(proxy_support)
3a、安装opener
    urllib.request.install_opener(opener)   # 一劳永逸
3b、调用opener
    opener.open(url)
'''



import urllib.request
import random

url1 = 'http://www.whatismyip.com.tw'

iplist = ['218.202.111.10:80', '111.11.122.7:80','111.13.136.36:80', '111.13.136.46:80','183.245.147.24:80']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)

# opener也可以修改headers
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0')]

opener.open(url1)

response = urllib.request.urlopen(url1)
html = response.read().decode('utf-8')

print(html)
