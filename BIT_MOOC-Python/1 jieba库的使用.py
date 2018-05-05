#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
jieba是优秀的中文分词第三方库。
中文文本需要通过分词获得单个的词语，利用一个中文词库，确定汉字之间的关联概率，
汉字间概率大的组成词组，形成分词结果，用户还可以添加自定义的词组。

@author: ZHOU Heng
"""

import jieba

print( jieba.lcut("中国是一个伟大的国家") )
print( jieba.lcut("中国是一个伟大的国家", cut_all=True) )
print( list(jieba.cut_for_search("中国是一个伟大的国家")) )


if __name__ == "__main__":
    pass