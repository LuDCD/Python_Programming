#!/usr/bin/env python
# -*- coding:utf8 -*-

# 是 requests，不是 request，有 s
import requests
from bs4 import BeautifulSoup
import re

r = requests.get( 'https://book.douban.com/subject/4913064/comments' )

# 打印状态码 200 为正常
# print( r.status_code )

soup = BeautifulSoup(r.text, 'lxml')
print( type(soup) )
print( dir(BeautifulSoup) )
pattern = soup.find_all('p', 'comment-content')

for item in pattern:
    print( item.string )