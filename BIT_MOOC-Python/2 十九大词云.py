#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
根据十九大报告 2CPC19th.txt 绘制词云

@author: ZHOU Heng
"""

import jieba
import wordcloud
from scipy.misc import imread

mask = imread('2CPCbadge.jpg')
# 打开文件
filename = '2CPC19th.txt'
with open(filename, 'r', encoding='utf-8') as f:
    t = f.read()

ls = jieba.lcut(t)
txt = ' '.join(ls)

# 产生WordCloud对象
w = wordcloud.WordCloud( font_path = "C:\Windows\Fonts\msyh.ttc", width=700, height=713, \
                         mask=mask, background_color='white')
# 生成词云
w.generate(txt)
# 输出到文件
w.to_file('2CPC19th_badge_wordcloud.png')



if __name__ == "__main__":
    pass



