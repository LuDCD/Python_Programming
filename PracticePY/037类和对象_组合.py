#!/usr/bin/python
# -*- coding:utf8 -*-

class Person:
    def __init__(self,number):
        self.number = number

class Student(Person):
    pass

class Teacher(Person):
    pass

class School:
    def __init__(self,NumberSt,NumberTea):
        self.student = Student(NumberSt)        # 把横向关系的类，用组合
        self.teacher = Teacher(NumberTea)

    def print_num(self):
        print( "学校里有学生 %d 名；老师 %d 名。" % (self.student.number,self.teacher.number) )

# 实例化、并调用
school = School(100,50)
school.print_num()


# 类、类对象、实例对象

# 如果属性名和方法名相同，属性会覆盖方法
class C:
    def x(self):
        pass

c = C()
# c.x = 8
# 由于Python变量可以不用声明就定义使用，所这里相当于在实例对象小c中创建了变量x,由于x和方法x()重名，所以方法不能再被调用
# c.x()       # TypeError: 'int' object is not callable


#
class A:
    count = 0


aa = A()
bb = A()
cc = A()

print('\nFirst')
print('aa.count = %d.' % aa.count)
print('bb.count = %d.' % bb.count)
print('cc.count = %d.' % cc.count)

cc.count +=10

print('\nSecond')
print('aa.count = %d.' % aa.count)
print('bb.count = %d.' % bb.count)
print('cc.count = %d.' % cc.count)

A.count += 100

print('\nThird')
print('aa.count = %d.' % aa.count)
print('bb.count = %d.' % bb.count)
print('cc.count = %d.' % cc.count)

# 可以从内存的角度去思考为什么.
# 因为你对类的实例化对象进行了赋值操作，Python会为自动为这个实例开辟一个新的空间
# 而其他的类的实例（aa、bb）由于没有进行任何操作所以仍然公用着类对象的空间，也就是A的空间。
# 这也就是为什么你对类对象A的count进行操作，实例对象aa、bb的count也会发生改变的原因。


# 可以用 对象.__dict__ 来查看对象的属性
print( 'A.__dict__:\n',A.__dict__ )
print( '\naa.__dict__:\n', aa.__dict__ )
print( '\nbb.__dict__:\n', bb.__dict__ )
print( '\ncc.__dict__:\n', cc.__dict__ )