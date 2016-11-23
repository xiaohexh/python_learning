#!/usr/bin/env python
# -*- coding=UTF-8 -*- 

# use merge sort algorithm to get number of reverse order pair
# a = [2, 9, 8, 12, 1]
# result = 5
# [2, 1][9, 1][9, 8][8, 1][12, 1]
# time complexity is O(N*logN) is better than O(N*N)

gcount = 0

def merge(a, beg, mid, end):

	global gcount
	
	tmp = []
	i = beg
	j = mid + 1
	while i <= mid and j <= end:
		if a[i] < a[j]:
			tmp.append(a[i])
			i += 1
		else:
			tmp.append(a[j])
			j += 1
			gcount += mid - i + 1

	while i <= mid:
		tmp.append(a[i])
		i += 1

	while j <= end:
		tmp.append(a[j])
		j += 1

	k = len(tmp)
	for i in range(k):
		a[beg + i] = tmp[i]

def merge_sort(a, beg, end):
	if beg < end:
		mid = (beg + end) / 2
		merge_sort(a, beg, mid)
		merge_sort(a, mid + 1, end)
		merge(a, beg, mid, end)


if __name__ == '__main__':

	a = [2, 9, 8, 12, 1]
	size = len(a)

	merge_sort(a, 0, size - 1)

	print "reverse order pair number:%d" % gcount
