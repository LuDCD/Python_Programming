#!/usr/bin/python
# -*- coding:utf8 -*-

def MyFirstFunction():
    ' 我是函数文档 ，我不会被打印 但我可以被使用方法打印出来 '
    print("我的第一个函数")

def addMe2Me( x ):
    return ( x+x )

MyFirstFunction()
print(MyFirstFunction.__doc__)     # 双下划线   方法一
help(MyFirstFunction)              #           方法二

a = int(input("输入一个数："))
add = addMe2Me(a);
print("%d + %d = %d" % (a,a,add))

#关键字参数
def sbLikesth(somebaby,something):
    print(somebaby + 'like' + something)

sbLikesth('周恒','吃饭')
sbLikesth(something="吃饭",somebaby='周恒')     #有了这些关键字就可以避免函数参数的顺序传入出错

#默认参数
def sbSays( name = "周恒", word = '静心竭力' ):
    print(name + " says that " + word)

sbSays()                 # 在不传入参数的时候选择默认参数
sbSays('列林','敌人是不会打瞌睡的。')
sbSays(word="believe youself!")

#可变参数
def test( *params ):
    print("参数的长度为："  , len(params))
    print('第一个参数为：',params[0])
    print('所有参数为：',params)

test(123,'zhouheng',222,34,'哈哈')

# 参数包含可变参数，但还有其他参数
def test2( keyargs,*params ):
    print('我不是可变的参数，我是确定的参数：',keyargs)
    print('所有可变参数为：', params )

test2('好巧，我也是确定的',123,'sb','周恒',455,4)

def test3(*params, keyargs):
    print('我不是可变的参数，我是确定的参数：',keyargs)
    print('所有可变参数为：', params )

test3(123,'sb','周恒',455,4, keyargs='好巧，我也是确定的')

# test3(keyargs='好巧，我也是确定的', 'sb','周恒',455,4 )  是失败的
# 建议把不变的参数放在最前面,像test2；如果不是最前面，就必须使用关键字参数



# Python函数的返回值

# 1、可以没有返回值
def HelloWorld():
    print("Hello World!")

temp = HelloWorld()
print(temp)
print(type(temp))

# 2、多个返回值。其实多个返回值只是表象，实际上把多个元素打包成一个列表或元组返回
def back():
    return [123,'qq','后']   # 返回的是列表

print(back())

def back2():
    return 123,'qq','后'     # 返回的是元组

print(back2())