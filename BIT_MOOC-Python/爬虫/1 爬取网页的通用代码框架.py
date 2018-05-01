#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
爬取网页的通用代码框架

@author: ZHOU Heng
"""

import requests

def getHTMLTxt(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except :

        return '产生异常'

def test():
    getHTMLTxt('www.baidu.com')
    getHTMLTxt('https://www.baidu.com')


if __name__ == "__main__":
    test()



