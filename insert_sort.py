#!/usr/bin/env python
# -*- coding = UTF-8 -*-

def insert_sort(a):

	size = len(a)

	for idx in range(1, size):

		tmp = a[idx]

		i = idx
		while i > 0 and a[i - 1] > tmp:
			a[i] = a[i - 1]
			i -= 1

		a[i] = tmp


if __name__ == '__main__':

	a = [45, 32, 4, 8, 98, 10]

	print "before insert sort:", a

	insert_sort(a)

	print "after insert sort:", a
