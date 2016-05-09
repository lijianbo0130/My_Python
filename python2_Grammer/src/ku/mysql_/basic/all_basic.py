#coding=utf-8
'''
数据库的所有基本操作
'''
 
import  MySQLdb    
   
#连接    
con=MySQLdb.connect(host="localhost",user="root",passwd="root",db="test",charset="utf8")  
cursor = con.cursor()    

#删除表
sql = "drop table if exists user"
cursor.execute(sql)

#创建
sql = "create table if not exists user(name varchar(128) primary key, created int(10))"
cursor.execute(sql)

#写入一条数据
sql = "insert into user(name,created) values(%s,%s)"   
param = ("aaa",22)    
n = cursor.execute(sql,param)    
print 'insert',n    
   
#写入多行    
sql = "insert into user(name,created) values(%s,%s)"  
#这里用的是(tuple,tuple)  用[tuple,tuple] 也可以 一般使用list
param = (("bbb",22), ("ccc",33), ("ddd",44))
n = cursor.executemany(sql,param)    
print 'insertmany',n    

#更新    
sql = "update user set name=%s where name='aaa'"   
param = ("zzz")    
n = cursor.execute(sql,param)    
print 'update',n    
   
#查询    
n = cursor.execute("select * from user")    
for row in cursor.fetchall():    
    print row
    for r in row:    
        print r    
   
#删除    
sql = "delete from user where name=%s"   
param =("bbb")    
n = cursor.execute(sql,param)    
print 'delete',n    

#查询    
n = cursor.execute("select * from user")    
print cursor.fetchall()    
  
   
#提交    
con.commit()
#关闭    
con.close()   