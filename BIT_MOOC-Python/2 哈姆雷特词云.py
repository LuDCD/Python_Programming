#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
统计哈姆雷特hamlet中出现的最多的词
形成词云

@author: ZHOU Heng
"""

import wordcloud

filename = '1hamlet.txt'
with open(filename, 'r', encoding='utf-8') as f:
    txt = f.read()

# banWordDict = {"thy", 'end', 'play', 'the', 'sleep', 'and', 'to', 'of', 'that',\
#                'this', 'in', 'it', 'has', 'have', 'you', 'his', 'him', 'her', 'them','they',\
#                'but','my', 'is', 'are', 'not', 'so', 'what', 'do', 'we', 'must', 'was' \
#                'as', 'for', 'all', 'with', }
# w = wordcloud.WordCloud( width=1000, height=900, stopwords=banWordDict, background_color = 'white')
w = wordcloud.WordCloud( width=1000, height=900, max_words=150, background_color = 'white')
w.generate(txt)
w.to_file("2Hamlet_wordcloud.png")

if __name__ == "__main__":
    pass


