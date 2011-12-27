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
        #连接时注意字符集为charset='utf8'
        conn = MySQLdb.Connection(host='localhost', user='root', passwd='marui555', db='PM', charset='utf8')
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

#管理部门
def add_depa(Dname):
    get_conn()
    cursor = conn.cursor()
    sql = "insert into Department(Dname) values ('%s')" % Dname
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def del_depa(Did):
    get_conn()
    cursor = conn.cursor()
    sql = "delete from Department where Did = '%s';" % Did
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def get_all_depa():
    get_conn()
    cursor = conn.cursor()
    sql = "select * from Department"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return dict(data)

def get_depa(Did):
    get_conn()
    cursor = conn.cursor()
    sql = "select * from Department where Did='%s'"%Did
    cursor.execute(sql)
    data = cursor.fetchall()
    print data
    cursor.close()
    conn.close()
    return dict(data)
    
def update_depa(Did, Dname):
    get_conn()
    cursor = conn.cursor()
    print Dname, Did
    sql = "update Department set Dname='%s' where Did='%s'"%(Dname,Did)
    cursor.execute(sql)
    cursor.close()
    conn.close()

#管理人员
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
