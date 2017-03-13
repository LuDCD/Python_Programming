#!/usr/bin/python
# -*- coding:utf8 -*-

import urllib.request

req = urllib.request.urlopen('http://placekitten.com/g/500/600')
'''
这两句和上面一句效果相同
res = urllib.request.Request(url, data, head)
req = urllib.request.urlopen(res)
'''
# urlopen(url)  中的url参数既可以为字符串也可为Request对象
# Open the URL url, which can be either a string or a Request object.
cat_imge = req.read()

with open('053cat_500_600.jpg', 'wb') as f:
    f.write( cat_imge )

'''
测试
print( req.geturl() )
print( req.info() )
print( req.getcode() )      # 200表示http状态，良好
'''