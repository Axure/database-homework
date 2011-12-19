#-*- encoding: utf-8 -*-
import os, sys, string
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='marui555',db='PM',charset='utf8')
Cursor = conn.cursor();
name = '\'123\''
sql = 'insert into Department(Dname) values (%s)' % name
sql.decode('utf-8')
Cursor = Cursor.execute(sql)

