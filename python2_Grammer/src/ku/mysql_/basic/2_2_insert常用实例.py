#coding=utf-8
'''
Created on 2015年7月22日
@author: Administrator
'''
import MySQLdb as db

# 连接数据库
conn=db.connect(host="localhost",user="root",port=3309,
                    passwd="123456",db="test",charset="utf8")  
cursor = conn.cursor()

#批量插入
a=[" 李四" , 24]
sql = " insert into users (name, age) values (%s, %s)" 
lis_insert=[]
for i in range (500):
    lis_insert.append(a)
    if i%10000==0:
        cursor.executemany(sql,lis_insert)
        conn.commit()
        lis_insert=[]
