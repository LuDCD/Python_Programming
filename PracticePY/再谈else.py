#!/usr/bin/python
# -*- coding:utf8 -*-

# while-else / for-else
def showMaxFact( num ):
    count = num // 2    # 地板除
    # 因为 num 的最大约数，最大为 num 的一半
    while count > 1:
        if num % count == 0:
            print('largest factor of %d is %d.' % (num, count))
            break   # 跳出while-else
        count -= 1
    else:
        print(num,'is prime.')


for eachNum in range(10,21):
    showMaxFact( eachNum )


# try-else
try:
    a = int( '123' )
    # b = int( 'abc' )
except ValueError as reason:
    print('出错了。\n错误为' + str(reason) )
else:
    print( 'No error!')


# with的用法
# 一般的异常处理
try:
    f = open('with_dome.txt', 'w')
    for each_line in f:
        print( each_line )
except OSError as reason:
    print( '出错了！错误为：' + str(reason) )
finally:
    f.close()

# 使用with
try:
    with open('with_dome.txt', 'w') as f:
        for each_line in f:
            print( each_line )
except OSError as reason:
    print( '出错了！错误为：' + str(reason) )


