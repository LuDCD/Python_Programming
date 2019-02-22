#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
在一个线程里实现并行效果。
基本的生产者和消费者模型

@author: ZHOU Heng
"""

import time

def producer():
    # 生成两个消费者
    user1 = consumer("Jake")
    user2 = consumer("Toma")

    # 消费者初始化
    user1.__next__()
    user2.__next__()

    # 开始生产
    for i in range(1,10):
        time.sleep(1)
        print("Producer:第{}个和第{}包子已经生产好！".format(i*2-1, i*2))
        user1.send(i*2-1)
        user2.send(i*2)


def consumer(consumer_name):
    print("{}准备就绪，坐等吃包子！".format(consumer_name))

    while True:
        baozi_index = yield
        print("\t第{}个包子，被{}吃了！".format(baozi_index, consumer_name))


def main():
    producer()


if __name__ == "__main__":
    main()