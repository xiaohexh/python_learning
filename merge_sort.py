#!/usr/bin/env python
# -*- coding = UTF-8 -*-

def merge(a, beg, mid, end, ret):

	k = 0 
	i = beg
	j = mid + 1

	while i <= mid and j <= end:

		if a[i] <= a[j]:
			ret[k] = a[i]
			i += 1

		else:
			ret[k] = a[j]
			j += 1

		k += 1

	while i <= mid:
		ret[k] = a[i]
		k += 1
		i += 1

	while j <= end:
		ret[k] = a[j]
		k += 1
		j += 1

	for idx in range(k):
		a[beg + idx] = ret[idx]

def merge_sort(a, beg, end, ret):

	if beg < end:

		mid = (beg + end) / 2
		merge_sort(a, beg, mid, ret)
		merge_sort(a, mid + 1, end, ret)
		merge(a, beg, mid, end, ret)

if __name__ == '__main__':

	a = [34, 12, 3, 9, 76, 43]
	ret = [0, 0, 0, 0, 0, 0]

	print "before merge sort: ", a

	merge_sort(a, 0, len(a) - 1, ret)

	print "after merge sort:  ", a
