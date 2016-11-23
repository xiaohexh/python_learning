#!/usr/bin/env python
# -*- coding=UTF-8 -*-
#
# some numbers in an array
# there is only two number(M, N) appear 1 time, 
# and others appear 2 times,
# find this two number(M, N)

def find_number_2(a):

	# calc xor result of M and N 
	tmp = 0
	size = len(a)
	for i in range(size):
		tmp ^= a[i]

	# 找出第一个是1的bit位（从低向高查找）
	for j in range(8):
		if (tmp >> j) & 1 == 1:
			break

	# 根据上面的计算将那一位为0和1的分成两组
	# 同时对不同的组进行异或运算，
	# 分别找出其中只出现一次的那个数字
	group1 = 0
	group2 = 0
	for i in range(size):
		if (a[i] >> j) & 1 == 1:
			group1 ^= a[i]
		else:
			group2 ^= a[i]

	print "number appear 1 time is: %d, %d" % (group1, group2)

if __name__ == '__main__':
	a = [3, 43, 9, 2, 3, 43, 5, 2]
	print a
	find_number_2(a)

