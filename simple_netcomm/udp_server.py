#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

address = ("127.0.0.1", 12345)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while True:
	data, addr = s.recvfrom(128)
	if not data:
		print "client is closed"
		break
	print "recv from :", data, "from", addr

s.close()
