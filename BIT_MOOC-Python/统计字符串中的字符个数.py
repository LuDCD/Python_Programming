#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
定义函数countchar()
按字母表顺序统计字符串中所有出现的字母的个数（允许输入大写字符，并且计数时不区分大小写）。

输入格式:字符串

输出格式：列表

输入样例：Hello, World!

输出样例：
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]

@author: ZHOU Heng
"""

aOrd = ord( 'a' )   # 小写字母
alphabet = []       # 字母表列表
for i in range(26):
    alphabet.append(chr(aOrd+i))

# print(alphabet)


countList = [0]*26
# print(countList)

def countchar(str):
    str1 = str.lower()
    for s in str1:
        if s in alphabet:
            k = ord(s) - aOrd   # 第 k 个字母
            countList[k] += 1
    return countList

if __name__ == "__main__":
    str = input()
    print(countchar(str))