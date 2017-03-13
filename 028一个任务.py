#!/usr/bin/python
# -*- coding:utf8 -*-
boy = []
girl = []
count = 1

f = open( '028record.txt')

for each_line in f:
    if each_line[:3] != '===':
        # 分割字符串
        (role,role_spoken) = each_line.split('：', 1)
        if role == '男':
            boy.append( role_spoken )
        if role == '女':
            girl.append( role_spoken )
    else:
        # 将上面分割好的字符串分开保存
        file_boy_name = '028boy_' + str(count) + '.txt'
        f_boy = open( file_boy_name ,'w')
        f_boy.writelines( boy )
        # f.write( str )    只能写入字符串;将字符串str写入文件
        # f.writelines( seq )   向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象
        f_boy.close()

        file_girl_name = '028girl_' + str(count) + '.txt'
        file_girl = open( file_girl_name ,'w')
        file_girl.writelines( girl )
        file_girl.close()   # 记得关闭文件

        count += 1
        boy.clear()
        girl.clear()

file_boy_name = '028boy_' + str(count) + '.txt'
f_boy = open( file_boy_name ,'w')
f_boy.writelines( boy )
f_boy.close()

file_girl_name = '028girl_' + str(count) + '.txt'
file_girl = open( file_girl_name ,'w')
file_girl.writelines( girl )
file_girl.close()

count += 1
boy.clear()
girl.clear()
