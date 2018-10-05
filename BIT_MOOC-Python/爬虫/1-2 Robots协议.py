#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Robots Exclusion Standard，网络爬虫排除标准

作用：
网站告知网络爬虫哪些页面可以抓取，哪些不行

形式：
在网站根目录下的robots.txt文件


@author: ZHOU Heng
"""

'''
例如：https://www.jd.com/robots.txt

User‐agent: *
Disallow: /?*
Disallow: /pop/*.html
Disallow: /pinpai/*.html?*
User‐agent: EtaoSpider
Disallow: /
User‐agent: HuihuiSpider
Disallow: /
User‐agent: GwdangSpider
Disallow: /
User‐agent: WochachaSpider
Disallow: /

Robots协议基本语法
# 注释，
*代表所有，
/代表根目录

User‐agent: *
Disallow: /

'''

def test():
    pass


if __name__ == "__main__":
    test()



