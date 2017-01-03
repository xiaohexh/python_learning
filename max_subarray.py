#!/usr/bin/env python
# -*- coding = UTF-8 -*-

def max_subarray(a):
	cur_left = 0
	cur_right = 0
	cur_max = 0

	left = 0
	right = 0
	max_sum = 0

	for i in range(len(a)):
		cur_max += a[i]
		if cur_max > 0:
			cur_right = i
			if max_sum < cur_max:
				left = cur_left
				right = cur_right
				max_sum = cur_max
		else:
			cur_max = 0
			cur_left = i + 1
			cur_right = i + 1

	# all number is negative
	if max_sum == 0:
		max_sum = a[0]
		for i in range(1, len(a)):
			if a[i] > max_sum:
				max_sum = a[i]
				left, right = i, i

	print 'left:%d right:%d max_sum:%d' % (left, right, max_sum)
	return max_sum

if __name__ == '__main__':
	#a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	a = [-2, -1, -3, -1, -2, -1, -5, -4]
	max_subarray(a)
