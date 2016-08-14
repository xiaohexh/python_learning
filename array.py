#!/usr/bin/python
# -*- coding: utf-8 -*-

# three type arrays:
# list/tuple/dictionary

# List
print "----------- List -------------"
alist = [3, "chris", 34, ["Shanghai", "ChangNing"]]
alist.append("Male")
alist.insert(3, 34.5)
alist += ["JS", "XZ"]
print alist
print alist[1:4]

print

# Tuple
print "----------- Tuple -------------"
atuple = (3, "chris", 34, ["Shanghai", "ChangNing"])
print atuple
print atuple[-3:-1]

print 

# Dictionary
print "----------- Dictionary -------------"
dict_arr = {'a':100, 'b':'Chris', 'c':[12, 34, 56]}
print "all keys:", dict_arr.keys()
print "all values:", dict_arr.values()

for k in dict_arr:
	v = dict_arr.get(k)
	print v
