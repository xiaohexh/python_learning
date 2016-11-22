#!/usr/bin/env python
# -*- coding = UTF-8 -*-

def select_sort(a):
	
	size = len(a)

	for i in range(size - 1):
		m_value = a[i]
		m_idx = i
		for j in range(i + 1, size):
			if a[j] < m_value:
				m_value = a[j]
				m_idx = j
		a[i], a[m_idx] = a[m_idx], a[i]


if __name__ == '__main__':

	a = [34, 5, 12, 32, 9, 7]

	print "before select sort:", a

	select_sort(a)

	print "after select sort: ", a
