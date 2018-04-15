#!/usr/bin/python
# -*- coding:utf8 -*-

# __init__(self[, ...]) 方法
class Person:
    # 有需求的话改写 __init__(self) 方法，没需求就不写
    def __init__(self,name='张三',age=100):
        self.name = name
        self.age = age
        # __init__(self) 默认的返回值为 None,不可修改，否则报错


person = Person('周恒',18)
# 对于类的实例化括号里的参数，除了self不用写之外，其他参数要不要写取决于__init__()方法的参数。
# 因为类Person后面括号里的参数是要传给__init__()方法的

# __new__(cls[, ...])

# __del__(self)
# del x 和 x.__del__() 不一样
# 只有当对象的所有引用都被删完的时候才会调用__del__()方法


# 工厂函数








