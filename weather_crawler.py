#!/usr/bin/env python2
#coding=utf-8

import urllib2
import re
import sys
import Queue
import threading
from bs4 import BeautifulSoup

# global 
workers=20
gq=Queue.Queue(maxsize=2*workers)
sq=Queue.Queue(maxsize=4*workers)
threads=[]

def getInfo(url):
    try:
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read().decode("gb18030"), 'lxml')
    except:
        print "Error"
        return
    
    # get address
    pp = soup.find('select', id='province').find('option', selected=True).string[2:]
    cc = soup.find('select', id='city').find('option', selected=True).string[2:]
    try:
        zz = soup.find('select', id='zone').find('option', selected=True).string[2:]
    except:
        zz = ""
    
    temp=soup.find('div', id='today').find("ul")
    htemp=temp.find("span").contents[0].string[:-1]
    ltemp=temp.find("span").contents[2].string[:-1]
    try:
        weather=temp.contents[7].string
        wind=temp.contents[9].string
    except:
        print "ERROR:",url, pp, cc, zz
        return

    info = pp + " " + cc + " " + zz + " " + "high temp:" + htemp + " low temp:" + ltemp + " weather:" + weather + " wind:" + wind + " "

    # get live info
    ll = soup.find('div', class_= 'w_box_sh')
    for ch in soup.find('div', class_='w_box_sh'):
        if ch.name != None:
            dch = ch.find('dl')
            xx = "%s %s %s " % (dch.contents[1].contents[0].string[:-1], dch.contents[1].contents[1].string, dch.contents[3].string)

            info += xx

    sq.put(info)

def workThread():
    while True:
        url=gq.get()

        if url=="over":
            exit() 
        getInfo(url)

def showwork():
    while True:
        info=sq.get()
        print info

### set coding
reload(sys)
sys.setdefaultencoding("utf-8")

### start worker thread
for i in range(workers):
    t=threading.Thread(target=workThread,args=())
    t.start()
    threads.append(t)

threading.Thread(target=showwork, args=()).start()

### entery
page = urllib2.urlopen("http://www.tianqi.com/chinacity.html")
pattern = '\s*<li><a href="(http://.*.tianqi.com/.*)" title=".*" target="_blank">(.*)</a></li>\s*'

for line in page.read().decode("gb18030").split('\n'):
    mm = re.match(pattern, line)
    if mm:
        gq.put(mm.group(1))

### wait thread over
for t in range(workers):
    gq.put("over")

for t in threads:
    t.join()

while True:
    if sq.empty() == True:
        break
    else:
        time.sleep(0.3)
        continue


print "Finish All!"

