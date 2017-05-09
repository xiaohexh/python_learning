#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 10080))
for i in range(100):
	s.send("I am client\n")
	data = s.recv(128)
	print i, ":recv from server:", data
	time.sleep(0.01)

s.close()
