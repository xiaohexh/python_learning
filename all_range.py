#!/usr/bin/env python
# -*- coding = UTF-8 -*-

#all range of 123 as follows:
# 123
# 132
# 213
# 231
# 312
# 321

count = 0

def all_range(a, k, m):

	global count

	if k == m:
		print "%d range:", a	
	else:
		i = k
		while i <= m:
			a[k], a[i] = a[i], a[k]
			all_range(a, k + 1, m)
			a[k], a[i] = a[i], a[k]
			i += 1

def foo(a):
	all_range(a, 0, len(a) - 1)

if __name__ == '__main__':

	a = [1, 2, 3]
	print "all range of ", a, " as follows:"
	foo(a)
