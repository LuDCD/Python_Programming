#!/usr/bin/python
# -*- coding:utf8 -*-


import io
import sys
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

import os

def url_open(url):
    req = urllib.request.Request( url )
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0')
    response = urllib.request.urlopen(url)

    html = response.read()
    return html

def get_page(url):

    html = url_open(url).decode('utf-8')

    flag1 = html.find('current-comment-page') + 23
    flag2 = html.find(']', flag1)

    return html[flag1:flag2]

def find_image(url):

    response =  url_open(url)
    html = response.decode('utf-8')

    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a,a+255)

        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=',b)

    return img_addrs

def save_image(folder, image_addrs):
    for each in image_addrs:
        file_name = each.split('/')[-1]
        with open(file_name,'wb') as f:
            img = url_open(each)
            f.write(img)



def download_mm(folder='OOXX', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"

    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'

        image_addrs = find_image(page_url)

        save_image(folder, image_addrs)

if __name__ == '__main__':
    download_mm()
