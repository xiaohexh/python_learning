#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from string_util import StringUtil

class StringUtilTestCase(unittest.TestCase):
	def setUp(self):
		self.su = StringUtil()
		self.info = "Andy|34|Shanghai"
	
	def tearDown(self):
		self.su = None

	def testSplit(self):
		delimiter = "|"
		self.assertEqual(self.su.Split(self.info, delimiter), ['Andy', '34', 'Shanghai'])

	def testFind(self):
		self.assertTrue(self.su.Find(self.info, "Shanghai"))

	def testCount(self):
		self.assertNotEqual(self.su.Count(self.info, "h"), 2)
		#self.assertEqual(self.su.Count(self.info, "h"), 2)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(StringUtilTestCase("testSplit"))
	suite.addTest(StringUtilTestCase("testFind"))
	suite.addTest(StringUtilTestCase("testCount"))

	return suite


if __name__ == '__main__':
	unittest.TextTestRunner().run(suite())
