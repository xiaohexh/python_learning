#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 12345))
s.listen(5)

while 1:
	cs,addr = s.accept()
	print "got connection from ", addr
	ra = cs.recv(512)
	print "recvd from client ", ra
	cs.send("Hello, I am server")
	cs.close()

s.close()
