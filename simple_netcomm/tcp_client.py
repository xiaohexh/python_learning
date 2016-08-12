#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))
s.send("I am client")
data = s.recv(128)
print "recv from server:", data
s.close()
