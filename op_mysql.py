#!/usr/bin/python
# -*- coding: utf-8 -*-

# pre-install dependent libraries
# 1) mysql_config environment
# ubuntu os
# sudo apt-get install libmysqlclient-dev
# sudo apt-get install python-dev
# centos
# yum install MySQL-devel
# yum install python-devel
# 2) MySQLdb
# tar zxvf MySQL-python-1.2.2.tar.gz
# cd MySQL-python-1.2.2
# sudo python setup.py build
# sudo python setup.py install
# 3) check install success or not
# $python
# >>> import MySQLdb
# No error happened

import MySQLdb

db = MySQLdb.connect(host='192.168.144.76',user='root',passwd='root000',port=3306,charset='utf8')

cur =db.cursor();

cur.execute('use figure_model_environment')

#table_pre = 'disaster_warning_atom_'
table_pre = 'future_weather_atom_'

table_num = 100
wind_power = 5

for i in range(table_num):

    table_name = table_pre + str(i)

    #select_cmd = 'select * from %s where wind_power > %d' % (table_name, wind_power)
    select_cmd = 'select * from %s' % (table_name)

    cur.execute(select_cmd)

    for row in cur.fetchall():
        print i 
        print row  
            
cur.close()
db.close()
