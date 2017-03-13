#!/usr/bin/python
# -*- coding:utf8 -*-


import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码


import urllib.request
import urllib.parse

content = input('请输入需要翻译的内容：')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'

data = {}       # 字典
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'    # 轻量级的数据交换格式
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode( data ).encode('utf-8')   # 把Unicode编码从utf-8的形式


req = urllib.request.urlopen(url,data)
html = req.read().decode('utf-8') # 把utf-8解码为Unicode形式

#print( html )
'''
{"type":"EN2ZH_CN","errorCode":0,"elapsedTime":3,"translateResult":[[{"src":"Iove","tgt":"爱"}]],"smartResult":{"type":1,"entries":["","大礼包","熊猫","是什么"]}}
'''

import json

target = json.loads( html )   # 变成了字典
# print( type(target) )

print( '翻译结果为：' )
print( target['translateResult'][0][0]['tgt'] )
