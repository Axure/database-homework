#-*- encoding: utf-8 -*-

###############################################################
#
#   处理数据库
#
###############################################################

import os, sys, string                  
import MySQLdb                          
from person_model import *

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
    cursor.close()
    conn.close()
    return dict(data)
    
def update_depa(Did, Dname):
    get_conn()
    cursor = conn.cursor()
    print Dname, Did
    sql = "update Department set Dname='%s' where Did=%d;"%(Dname, int(Did))
    print sql
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

# 管理人员
# 获取所有人员
def get_all_person():
    get_conn()
    cursor = conn.cursor()
    person = []
    sql = "select * from Person"
    cursor.execute(sql)
    data = cursor.fetchall()
    data = list(data)
    for ss in data:
        depa_name = get_depa(ss[3])[ss[3]]
        temp_dict = {'Pid':ss[0],'Pname':ss[1],'Psex':ss[2],'Ddepa':ss[3],'Psalary':ss[4], 'Pwork':ss[5],'Pdismiss':ss[6], 'Dname':depa_name}
        person.append(temp_dict)
        # print get_depa(ss[3])[ss[3]]
    cursor.close()
    return person

# 添加人员
def add_person(person):
    get_conn()
    cursor = conn.cursor()
    sql = "insert into Person(Pname, Psex, Pdepa, Psalary, Pwork, Pdismiss) values ('%s', '%s', %s, %s, '%s', '%s')"%(person['name'], person['sex'], person['depa'], person['salary'], person['work'], person['dismiss'])
    print sql
    for kk in person:
        print kk, person[kk]
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()   

def del_person(Pid):
    get_conn()
    cursor = conn.cursor()
    sql = "delete from Person where Pid = '%s';" % Pid
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()   

def update_person(person):
    get_conn()
    cursor = conn.cursor()
    sql = "update Person set Pname='%s', Psex='%s', Pdepa='%s', Psalary='%s', Pwork='%s', Pdismiss='%s' where Pid='%s'"%(person['Pname'], person['Psex'], person['Pdepa'], person['Psalary'], person['Pwork'], person['Pdismiss'], person['Pid'])
    print sql 
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def get_ppperson():
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
