#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import os

### set coding
reload(sys)
sys.setdefaultencoding("utf-8")

content = '<a target="blank" href="http://blog.ithomer.net">ithomer</a>'  
match = re.compile(r'(?<=href=["]).*?(?=["])')  
print re.findall(match, content)        # ['http://blog.ithomer.net']
