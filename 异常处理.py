#!/usr/bin/python
# -*- coding:utf8 -*-

# try 一旦检测到异常，下面的语句就不会执行
try:
    f = open( '我是一个文件.txt' )
    print( f.read() )
    f.close()

    i = 1 + '1'     # TyptError

except (OSError,TypeError) as error:
    print( '文件访问失败。\n原因是：' + str(error) )



'''
try:
    检测范围
except Exception [as reason]:
    出现异常(Exception)后的处理代码
finally:
    无论如何都会被执行的代码    # 比如关闭文件
'''





