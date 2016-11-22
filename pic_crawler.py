#!/usr/bin/env python
# -*- coding = UTF-8 -*-

import sys
import urllib
import urllib2
import re

class PicCrawler:

	OK = 0
	ERR = 1

	_targetURL = ""
	_htmlPage = ""

	def __init__(self, url):
		self._targetURL = url

	def getHtml(self):

		req = urllib2.Request(self._targetURL)

		page = urllib2.urlopen(req)

		self._htmlPage = page.read()

		if not self._htmlPage:
			return self.ERR

		return self.OK

	def getImg(self):
		ret = self.getHtml()
		if self.ERR == ret:
			print "Get %s page failed!" % self._targetURL
			return

		reg = r'src="(.+?\.jpg)" alt'
		imgre = re.compile(reg)

		imglist = re.findall(imgre, self._htmlPage)

		x = 0
		for imgurl in imglist:
			urllib.urlretrieve(imgurl, '%s.jpg' % x)
			x += 1

if __name__ == '__main__':

	picURL = "http://www.ivsky.com/"

	pc = PicCrawler(picURL)
	pc.getImg()
