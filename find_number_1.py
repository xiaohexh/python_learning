#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# some numbers in an array
# there is only one number(N) appear 1 time, 
# and others appear 2 times,
# find this number(N)

def find_number_appear_1(a):
	size = len(a)
	ret = 0
	for i in range(size):
		ret ^= a[i]

	print "number appear 1 time is:", ret

if __name__ == '__main__':
	a = [3, 43, 1, 9, 3, 43, 1]
	print a
	find_number_appear_1(a)

