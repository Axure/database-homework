#-*- encoding: utf-8 -*-

###############################################################
#
#   处理数据库
#
###############################################################

import os, sys, string                  
import MySQLdb                          

#初始化数据库连接
def get_conn():
    global conn
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='marui555', db='PM')
    except Except,e:
        print e;
        sys.exit()

def modify_passwd():
    pass

#验证管理员
def check_user(name, passwd):
    get_conn()
    cursor = conn.cursor()
    sql = "select * from user where name ='%s' and passwd='%s'"%(name,passwd)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    if data == () :
        return False
    else:
        return True

def add_person():
    pass
def del_person():
    pass
def modify_person():
    pass

def get_person():
    pass
def search_person():
    pass

def add_tax():
    pass
def add_bonus():
    pass
def add_fine():
    pass
def account_salary():
    pass
def kk():
    print "dd"
