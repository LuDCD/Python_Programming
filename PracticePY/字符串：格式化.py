#!/usr/bin/python
# -*- coding:utf8 -*-

# http://bbs.fishc.com/forum.php?mod=viewthread&tid=39140&extra=page%3D1%26filter%3Dtypeid%26typeid%3D403

a = int(input("请输入两个数：a="))
# a = int(input("a="))
b = int(input("b="))

print('%d + %d = %d' % (a,b,a+b))
print("%d + %d = %#o" % (a,b,a+b))
print("%d + %d = %#x" % (a,b,a+b))
#   ①单引号、双引号都可以
#   ②不是逗号，中间的连接是 %
#   ③后面是元组(a,b,a+b)

print(123456789)
print("%5.1f" % 3.14159)    # %m.nf m表示数字总宽度，包含小数点
print("%-5.1f" % 3.14159)
print("%.2f" % 3.14159)
