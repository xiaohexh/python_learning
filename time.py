#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

# strftime/strptime

# %d  Day of month as decimal number (01 - 31)
# %m  Month as decimal number (01 - 12)
# %Y  Year with century, as decimal number

# %S  Second as decimal number (00 - 59)
# %M  Minute as decimal number (00 - 59)
# %H  Hour in 24-hour format (00 - 23)

t = datetime.now()
print t
print t.strftime("%Y-%m-%d %H:%M:%S")
