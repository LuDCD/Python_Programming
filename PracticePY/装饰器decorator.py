#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
装饰器功能：统计函数运行时间

@author: ZHOU Heng
"""

import time

def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        # print(return_value)
        end_time = time.time()
        print("time of function running is {}".format(end_time - start_time))

        return res

    # timmer()函数返回的是函数warrper的引用，而不是调用warrper
    return warpper # √
    # return warrper()  # ×

# 装饰器也可以有自己的参数
@timmer  # test1 = timmer(test1)
def test1(name):
    print(name)
    print("test1 start")
    time.sleep(3)
    print("test1 end")

    return "test1 return"


if __name__ == "__main__":
    res = test1("zh")
    print(res)