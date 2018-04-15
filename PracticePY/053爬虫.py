#!/usr/bin/python
# -*- coding:utf8 -*-


'''
 URL的一般格式：
 protocol://hosthome[:port]/path/[;parament][?query]#fragment
 三部分组成
 1、协议（protocol）：http，https，ftp，ed2k，...
 2、存放资源的服务器的域名系统或IP地址（有时候要包含端口号，各种传输协议都有默认的端口号，如http的默认端口号为80）
 3、资源的具体地址，如目录或者文件名等
'''

# http://blog.csdn.net/jim7424994/article/details/22675759
import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

import urllib.request

req = urllib.request.urlopen('http://www.baidu.com')

html = req.read()   # 对象req有read()方法
# print( dir(req))
# print( html )

html = html.decode('UTF-8')
print(html)


'''
 urllib包

'''











