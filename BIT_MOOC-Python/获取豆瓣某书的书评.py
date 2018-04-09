#!/usr/bin/env python
# -*- coding:utf8 -*-

#!/usr/bin/env python
# -*- coding:utf8 -*-

# 是 requests，不是 request，有 s
import requests
from bs4 import BeautifulSoup
import re

# 活着 book_id：4913064
r = requests.get( 'https://book.douban.com/subject/4913064/comments' )

# 打印状态码 200 为正常
# print( r.status_code )

soup = BeautifulSoup(r.text, 'lxml')

# 抓取评论
pattern = soup.find_all('p', 'comment-content')


for item in pattern:
    print( item.string )


# 抓取评论星书
starSum = 0
pattern_s = re.compile( '<span class="user-stars allstar(.*?)rating"' )
p = re.findall(pattern_s, r.text)

for star in p :
    starSum += int(star)

print( starSum )