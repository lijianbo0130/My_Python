#coding=utf-8
'''
Created on 2015年6月4日
@author: Administrator
'''
from __future__ import  division
import MySQLdb as db

#连接数据库
connnect=db.connect(host="localhost",user="root",port=3309,
                    passwd="123456",db="wuhandaxue2",charset="utf8")  
cursor = connnect.cursor()

sql = "set interactive_timeout=24*3600";
cursor.execute(sql)
print "down"