#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

def test_set():
	# string to set
	x = set('ithomer')
	y = set(['i', 't', 'h', 's', 'n'])  
	print("%s, %s" % (x, y))

	# intersection
	print ("%s" % (x & y))

	# union
	print ("%s" % (x | y))

	# difference
	print ("%s" % (x - y))
	print ("%s" % (y - x))

	# list to set
	tmp = [12, 34, 23, 56, 78, 15]
	nums = set(tmp)

	# iterate set
	print "iterate set"
	for num in nums:
		print num,
	print

	# add elem
	print "add elem"
	nums.add('h')
	print nums

	# del elem
	print "del elem"
	nums.remove('h')
	nums.discard(12)
	print nums

	print len(nums)

	# pop head
	print "pop head"
	nums.pop()
	print nums
	
	# shadow copy
	print "shadow copy"
	another = nums.copy()
	print another

	# clear set
	print "clear set"
	nums.clear()

if __name__ == "__main__":
	test_set()
