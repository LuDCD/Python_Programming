#!/usr/bin/python
# -*- coding:utf8 -*-

import re

# 正则表达式是以字符串的形式描述的
# 空格不能乱用，慎用

# seach()方法，用于在字符串中搜索正则表达式模式第一次出现的位置
# 记得要有 r
res = re.search(r'xing','xingongshiyanshi')
print(res)

# 通配符 . (元字符)
res2 = re.search(r'.n','xingongshiyanshi')
print( res2 )

# 可以用 \ 来消除 . 的通配功能
res3 = re.search(r'\.x','www.xy.com')
print( res3 )

# 用 \d 匹配日益任意的数字
res4 = re.search(r'\d','www.xy3245.com')
print(res4)

res5 = re.search(r'\d\d\d','www.xy3245.com')    # 匹配324
print( res5 )

# 匹配ip地址
res6 = re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.101.123')
print( res6 )


# 字符类
# 字符类中的任何一个匹配成功就算匹配成功
res6 = re.search(r'[AaEeIiOoUu]','www.baidu.com')   # 默认大小写敏感（可以修改）
print(res6)

# - 表示范围
res7 = re.search(r'[a-z]', 'WWW.abc.com')
print(res7)
res72 = re.search(r'[0-9]', 'WWW.123bai.com')
print(res72)
res73 = re.search(r'[2-9]', 'WWW.123bai.com')
print(res73)

# 限定重复匹配的次数{n,m}
res8 = re.search(r'ab{3}c','abbbcdef')      # b{3}表示b要重复3次
print(res8)
# 区别 re.search(r'(ab){3}c','abbbcdef')
res83 = re.search(r'(ab){3}c','abababcbcdef')
print(res83)

res82 = re.search(r'ab{3,10}c','abbbbbbbcdef')  # b{3,10}表示可以重复3-10次
print(res82)

# 匹配0-255
res9 = re.search(r'[01]\d\d|2[0-4]\d|25[0-5]','125')    # 匹配的都是字符串，数字也是字符串
print(res9)

# 匹配IP地址
ares = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', \
                 '192.168.1.1')     # r在引号外面
print(ares)


'''
 |
'''
bres = re.search(r'fish(C|D)','fishC')
b2res = re.search(r'fish(C|D)','fishD')
print(bres)
print(b2res)


'''
^ 脱字符,匹配输入字符串的开始位置
'''
cres = re.search(r'^fish','www.fish.com')
c2res = re.search(r'^fish','fish.com')
print(cres)
print(c2res)


'''
$ 匹配字符串的结束位置
'''
dres = re.search(r'fish$','www.fish.com')
d2res = re.search(r'fish$','www.fish')
print(dres)
print(d2res)


'''
\
1、将一个普通字符变成特殊字符，如\b表示匹配所有十进制数字
2、解除元字符< [ ] >的特殊功能，例如 \. 表示匹配点号本身
3、引用序号对应子组所匹配的字符串
'''


'''
^
'''

'''
\b 匹配一个单词的边界，单词被定义为Unicode的字母数字下划线字符
e.g. r'\bfishC\b' 会匹配字符串 'love FishC'、'fishC'、或 '(fishC)'
'''
eres = re.findall(r'\bfishC\b','I love fishC.com fishC_fishC(fishC)')
# 只匹配了前后两个
print(eres)


'''
\B 与\b相反，匹配非单词边界
e.g. r'py\B' 会匹配字符串'python'、'py3'、'py2';但是不会匹配'py '、'py.'、'py!'
'''

'''
\w 匹配Unicode的单词字符基本上所有语言的字符都可以匹配，当然也包括数字和下划线。
'''
fres = re.findall(r'\w','我爱你(Python_RE)')
print(fres)


# ----------------------------------------------------------------------
# 模式对象
p = re.compile(r'[A-Z]')    # 编译
print(type(p))

# 模式对象的search方法，可以省去匹配的正则表达式
reas = p.search('Python123ZH')
print(reas)

reas2 = p.findall('Python123ZH')
print(reas2)
