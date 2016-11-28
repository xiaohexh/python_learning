#!/usr/bin/env python
# -*- coding=UTF-8- -*-
#
# description:
# 给定一数组a[N]，我们希望构造数组b [N]，其中b[j]=a[0]*a[1]…a[N-1] / a[j]，
# 在构造过程中，不允许使用除法：
# 要求O（1）空间复杂度和O（n）的时间复杂度；
# 除遍历计数器与a[N] b[N]外，不可使用新的变量（包括栈临时变量、堆空间和全局静态变量等）；

def create_array_from_another(a):
	b = []
	size = len(a)
	tmp = 1
	b.append(tmp)
	for i in range(1, size):
		tmp *= a[i]
		b.append(b[i - 1] * a[i - 1])
		# b[0] = 1
		# b[1] = b[0] * a[0] = a[0]
		# b[2] = b[1] * a[1] = a[0] * a[1]
		# b[3] = b[2] * a[2] = a[0] * a[1] * a[2]
		# b[4] = b[3] * a[3] = a[0] * a[1] * a[2] * a[3]
		# ...
	
	tmp = 1
	idx = size - 2
	while idx >= 0:
		tmp *= a[idx + 1]
		b[idx] *= tmp
		idx -= 1

	print b

if __name__ == '__main__':
	a = [3, 2, 7, 8, 5]
	create_array_from_another(a)
