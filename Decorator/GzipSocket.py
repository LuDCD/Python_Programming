#!/usr/bin/python
# -*- coding:utf8 -*-

# 装饰器2
import gzip
from io import BytesIO

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self,data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode='w')
        zipfile.write(buf)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()