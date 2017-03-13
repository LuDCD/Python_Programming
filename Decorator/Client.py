#!/usr/bin/python
# -*- coding:utf8 -*-

# client 客户端
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',2401))
print("Receive: {0}".format(client.recv(1024)))
client.close()


