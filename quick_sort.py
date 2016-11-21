#!/usr/bin/python
# -*- coding: utf-8 -*-

import pdb
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# quick sort
a = [18, 9, 19, 28, 3, 5, 30]

def partition(a, beg, end):

	pivot = a[beg]
	i = beg
	j = end

	while i != j:

		while a[j] >= pivot and j > i :
			j -= 1

		while a[i] <= pivot and i < j:
			i += 1

		if i < j:
			a[i], a[j] = a[j], a[i]

	a[beg], a[i] = a[i], a[beg]
	
	return i
		

def quick_sort(a, beg, end):
	if beg > end:
		return
	pindex = partition(a, beg, end)
	quick_sort(a, beg, pindex - 1)
	quick_sort(a, pindex + 1, end)

if __name__ == '__main__':
	print "before quick sort: ", a

	quick_sort(a, 0, len(a) - 1)

	print "after quick sort:  ", a
