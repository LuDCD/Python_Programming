#!/usr/bin/python
# -*- coding:utf8 -*-

class ListNode():
    def __init__(self,data):
        self.data = data
        self.nextList = ListNode(data)

    def getValue(self):
        return self.data

    def setValue(self,value):
        self.data = value

class List():

    class ListNode():
        def __init__(self,data):
            self.data = data
            self.nextListNode = None

        def getValue(self):
            return self.data

        def setValue(self,value):
            self.data = value

    head = None
    end = None

    # def __init__(self,num):
    #     if i == 1:
    #         head = ListNode()
    #     for i in num:
    #         pass

    def Add(self, ListNode):
        if self.head == None:
            self.head = ListNode
            if self.end == self.head:
                self.ListNode = ListNode
                self.end = ListNode.nextListNode



