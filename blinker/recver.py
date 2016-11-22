#!/usr/bin/env python
#coding=utf-8

from blinker import Signal

def subscriber(sender):
    print("got a signal sent by %r" % sender)

if __name__ == '__main__':
    ready = Signal('ready')
    ready.connect(subscriber)
