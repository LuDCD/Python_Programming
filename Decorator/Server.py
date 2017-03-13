#!/usr/bin/python
# -*- coding:utf8 -*-

import socket

# 对导入的是一个装饰器（函数）
# 不能写成import Decorator.LogSocket
from Decorator.LogSocket import LogSocket


def respond(client):
    response = input("Enter a value:")
    client.send(bytes(response, 'utf8'))
    client.close()



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(LogSocket(client))
        # respond(client)
finally:
    server.close()