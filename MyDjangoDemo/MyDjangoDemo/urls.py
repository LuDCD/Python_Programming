"""MyDjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

#!/usr/bin/python
# -*- coding:utf8 -*-

from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^blog/index2/$',views.index2),
    url(r'^blog/index22/$',views.index22),  # 逗号不能忘！
    url(r'^blog/index23/$',views.index23),
    # url(r'^blog/index1/(?P<id>\d{2})/$',views.index1),
    # 第一个参数是正则表达式模板，第二个参数是处理方法
    # (?P<name>...)/分组除了原有的编号外再指定一个额外的别名
    # 参数传递

]
