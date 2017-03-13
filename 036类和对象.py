#!/usr/bin/python
# -*- coding:utf8 -*-

# 对象 = 属性 + 方法

# 一个类的简单例子
class PersonFirst:   # Python中约定：类名大写字母开头。函数名小写字母开头
    # 属性
    name = 'zhangsan'
    age = 18

    # 方法
    def eat(self):
        print('我有吃的功能。')

    def sleep(self):
        print('我有睡觉的方法。')


# 实例化
person1 = PersonFirst()
# 由于上面没有重写 __init__(self) 方法，Python默认的初始化，所以不用传参数
person1.eat()
person1.sleep()

# self
# 类中的每个方法都必须带上self参数，其他参数随你。


# __init__( self )
class PersonSecond:
    def __init__(self, name = '<默认的名字>'):   # 设置默认的参数可以防止在实例化对象的过程中没有传参的错误
        self.name = name
    def eat(self):
        print( '我是%s,我有吃的功能。' % self.name )
    def sleep(self):
        print( '我是%s, 我有睡觉的方法。'% self.name )

person2 = PersonSecond('张三')    # 传入姓名
person2.eat()
person2.sleep()


person21 = PersonSecond()        # 不传入参数，他会使用默认参数
person21.eat()


class PersonThird:
     # name mangling 名字改编，名字重整
     __age =  100   # Python 使用双下划线来私有化变量

     def getAge(self):
         return self.__age

person3 = PersonThird()
# person3.__age   # 访问不了
print( person3.getAge() )
print( person3._PersonThird__age )
# 其实Python干的就是把 __age 转化为 _类名__变量名,并未实现真正的私有









