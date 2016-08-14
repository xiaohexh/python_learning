#!/usr/bin/python
# -*- coding: utf-8 -*-

str = 'addpersontoour'

# substring
print str[5]
print str[0:4]
print str[-3:-1]
print str[6:]
print str[:-2]

# cat
str += "_postfix"
print str

# repeat
print str * 3

# length
print len(str)

# empty
if not str:
	print "Empty string"
else:
	print str
