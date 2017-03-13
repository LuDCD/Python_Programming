#!/usr/bin/python
# -*- coding:utf8 -*-

# --------------------------------------------------------------
# issubclass(class, classinfo)
# 判断 class 是不是 classinfo 的子类
# ①一个类被认为是其自身的子类
# ②classinfo可以是类对象组成的元组
class A:
    pass

class B(A):
    pass

print( issubclass(B,A))
print( issubclass(A,object) )
print( issubclass(A,A) )


# --------------------------------------------------------------
# isinstance(object, classinfo)
# 检查实例对象object属不属于 classinfo 类
# ① 如果第一个参数不是对象，永远返回False
# ② classinfo可以是类对象组成的元组
# ③ 如果第二个参数不是类或者类对象组成的元组，会抛出一个TypeError异常

bb = B()
print( '\nisinstance(bb,B):', isinstance(bb,B) )


#-------------------- -------------------------------------------
# hasattr(object,name)      # attr = attribute:属性
# 测试对象object里是否有名为name的属性
# 变量名要用引号括起来
class C:
    def __init__(self,x=0):
        self.x = x

cc = C(55)

# print( hasattr(cc,x))       # NameError: name 'x' is not defined
print( hasattr(cc,'x'))


#-----------------------------------------------------------------
# getattr(object,name[, default])
# 获得对象object的名为name属性的值。如果没有名为name的属性，AttributeError异常；如果有default参数，则返回default
print( getattr(cc,'x') )
# print( getattr(cc,'y') )    # AttributeError: 'C' object has no attribute 'y'
print( getattr(cc, "y", '不存在你访问的属性') )


# ----------------------------------------------------------------
# setattr(object, name, value)
# 设置对象object名为name属性的值为value。如果名为name的属性不存在，就新建一个，并赋值。
# name 仍然要引号

setattr(cc, 'y', 222)
setattr(cc, 'z', 'Zhouheng2018')
print( getattr(cc,'y') )
print( getattr(cc,'z') )


# ----------------------------------------------------------------
# delattr(object, name)
# 删除对象object中名为name的属性。如果属性name不存在，则抛出AttributeError异常
delattr(cc,'y')


# ----------------------------------------------------------------
# property(fget=None, fset=None, fdel=None, doc=None)
# 通过属性来设置属性.返回值为一个属性
class D:
    def __init__(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self,age):
        self.__age = age

    def delAge(self):
        del self.__age

    x = property( getAge(), setAge(), delAge() )

dd = D()


# ------------------------- enumerate
# 使用for循环对某个迭代对象遍历时，无法访问当前项目的索引。
# 但是穷举函数enumerate可以创建一个元组列表，
# 每个元组的第1个对象就是索引，第2个是原始条目的内容。
list = range(10)

for index, line in enumerate(list):
    print(index, line , end='\n')


