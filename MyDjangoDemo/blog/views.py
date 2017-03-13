#!/usr/bin/python
# -*- coding:utf8 -*-

from django.shortcuts import render

# Create your views here.


from django.template import loader,Context
from django.http import HttpResponse

# 使用模板的第一种方式：载入模板->创建Context对象->渲染模板->输出
def index2(request): # index(request)的 request参数必须要写

    # 导入模板文件
    t = loader.get_template('index2.html')

    # 创建Context对象
    c = Context( {'uname':'使用模板的第1种方式'} )
    # Context 对象的作用是：添加我需要向模板中渲染的数据

    # 对我们的模板进行渲染，调用render方法
    html = t.render(c)

    return HttpResponse(html)


# 使用模板的第二种方式：
from django.template import Template
def index22(request):
    t = Template('<h1>hello {{ uname }}</h1>')  # 直接通过Template类对象生成我们的模板对象
    c = Context( {'uname':'使用模板的第二种方式'} )
    html = t.render(c)

    return HttpResponse(html)


# 使用模板的第 三 种方式：
from django.shortcuts import render_to_response
def index23(request):
    return render_to_response('index2.html',{'uname':'AAA使用模板的第 三 种方式'})
    # 第一个参数是 对应的模板文件；第二个参数本质上是我们的Context对象
    # 上面这句话执行的结果就是HttpResponse对象



"""
from django.http import HttpResponse
from django.shortcuts import render_to_response

class Person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def say(self):
        return '我的名字是' + self.name


def index1(request,id):     # 这里的index方法是和urls.py中的index相对应的
    # req 参数表示视图处理方法接收的请求信息，请求信息封装在我们的req函数里面的

    # return HttpResponse('<h1>Hello welcome to django!</h1>')
    # 我们引用了HttpResponse对象,所以要导入

    # 使用模板文件

    user_dict = {'name':'zhhhh','age':23,'sex':'male'}
    user = Person('zeeee',3333,'male')
    book_list = ['python','java','php','web']
    return render_to_response('index1.html',{'title':'my page','user_dict':user_dict,'user':user,'book_list':book_list,'id':id})  # 键对应着模板变量
    # 传递的可以是 普通变量、列表、字典、对象的属性、对象的方法（方法没有参数有确定的返回值）、
    # 优先级为 字典 > 对象的属性 > 对象的方法 > 列表
"""

