#!/usr/bin/python
# -*- coding: utf-8 -*-

class StringUtil:
	def __init__(self):
		pass

	# split 'string' with 'delimiter'
	# Return a list
	def Split(self, string, delimiter):
		return string.split(delimiter)

	# find 'substr' exist in 'string'
	# Return True-find; False-not find
	def Find(self, string, substr):
		if string.find(substr) == -1:
			return False
		return True

	# count 'substr' appear times in 'string'
	# Return # count
	def Count(self, string, substr):
		return string.count(substr)

if __name__ == '__main__':
	su = StringUtil()
	info = "Andy|34|Shanghai"
	print su.Split(info, "|")
	print info
	print su.Find(info, "Andy")
	print su.Count(info, "a")
