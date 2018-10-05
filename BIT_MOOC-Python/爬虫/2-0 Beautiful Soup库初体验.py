#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
安装 beautifulsoup4 ,网址为 https://www.crummy.com/software/BeautifulSoup/

然后这样导入 beautifulsoup4 库：
form bs4 import BeautifulSoup

@author: ZHOU Heng
"""

import requests
from bs4 import BeautifulSoup


r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')       # parser：语法分析器

print( soup.prettify() )

if __name__ == "__main__":
    pass



