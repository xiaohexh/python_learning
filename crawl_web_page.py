#!/usr/bin/python
# -*- coding: utf-8 -*-

import os 
import sys
import urllib, urllib2
import shutil 
import requests 
import re 
from bs4 import BeautifulSoup  # BeautifulSoup解决中文乱码

### set coding
reload(sys)
sys.setdefaultencoding("utf-8")

headers = { 'Use-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' }  

# url = "http://blog.ithomer.net"  
url = "http://www.tianqi.com/chinacity.html"

# without 'headers' parameter
#req = urllib2.Request(url)

# 网站禁止爬虫，不能抓取或者抓取一定数量后封ip
# 解决：伪装成浏览器进行抓取，加入headers
req = urllib2.Request(url, headers = headers)

content = urllib2.urlopen(req).read()
# 一般网页的编码会在<meta>标签中标出;
# 目前有三种，分别是GB2312，GBK，GB18030，三种编码是兼容的。
# 从包含的中文字符个数比较：GB18030 > GBK > GB2312
content = BeautifulSoup(content, from_encoding='GB18030')
#print content
content.prettify()

# http://guilin.tianqi.com
rawlv2 = content.findAll(href=re.compile(r'^http://*.tianqi.com*'))
for page in rawlv2:
	print page
#rawlv2 = content.findAll(target=re.compile(r'lank$'))
#print rawlv2

# parse content with bs4
