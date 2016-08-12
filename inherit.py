#!/usr/bin/python
# -*- coding: utf-8 -*-

class SchoolMem:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print "init name:", self.name

	def tell(self):
		print 'name:%s, age:%d' % (self.name, self.age)

class Teacher(SchoolMem):
	def __init__(self, name, age, salary):
		SchoolMem.__init__(self, name, age)
		self.salary = salary

	def tell(self):
		SchoolMem.tell(self)
		print 'salary:', self.salary

class Student(SchoolMem):
	def __init__(self, name, age, score):
		SchoolMem.__init__(self, name, age)
		self.score = score

	def tell(self):
		SchoolMem.tell(self)
		print 'score:', self.score

if __name__ == '__main__':
	t = Teacher('chris', 30, 32)
	s = Student('andy', 23, 23.4)

	mems = [t, s]
	for mem in mems:
		mem.tell()
