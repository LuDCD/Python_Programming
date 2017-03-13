#!/usr/bin/python
# -*- coding:utf8 -*-

# http://bbs.fishc.com/forum.php?mod=viewthread&tid=45279&extra=page%3D1%26filter%3Dtypeid%26typeid%3D403

# f = open('D:\\zhouheng\\程序设计\\Python\\Programming\\file1.txt')
f = open('file1.txt')   # 如果不标路径他会在当前路径下查找
print( f )

# print( list(f) )

# f.read( size )  方法
print( f.read(5) )

print( '初始文件指针：', f.tell() )
print( '第一次读：\n', f.read() )
print( '第一次文件读完后的文件指针：', f.tell() )
print( '第二次读：\n', f.read() )
print( '第二次读后的文件指针：', f.tell() )

# f,seek( offset, from)
# 在文件中移动文件指针，从from（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节
f.seek(0, 0)
print( list(f) )

f2 = open('028test.txt', 'w')
f2.write('我是周恒。')
f2.close()









