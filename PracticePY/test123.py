#!/usr/bin/env python
# -*- coding:utf-8 -*-
#coding=utf-8
import urllib

import re
def getHtml(url):
    page = urllib.urlopen(url)
    #打开网址 html = page.read()
    # #读取网页内容，保存到htlm中

    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'#正则表达式
    imgre = re.compile(reg) #把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)#读取html 中包含 imgre（正则表达式）的数据
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)#直接将远程数据下载到本地
        x+=1
        html = getHtml("http://tieba.baidu.com/p/2460150866")
        print(getImg(html))

