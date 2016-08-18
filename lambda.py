#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1 param
p = lambda x : x ** 3
print p(3)

# multi-params
sum = lambda a, b : a + b
print sum(4, 5)

num = [8, 3, 2, 4, 9]
print [x for x in num if x % 2 == 0]
