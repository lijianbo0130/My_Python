#coding=utf-8
'''
简单插入
'''
import MySQLdb as db

# 连接数据库
conn=db.connect(host="localhost",user="root",port=3309,
                    passwd="123456",db="test",charset="utf8")  
cursor = conn.cursor()

# 直接插入一条
# cursor.execute("insert into users values('john',70)")


# 变成语句执行
# sql = "insert into users (name, age) values ('%s', %d)" % (" 张三" , 21) 
# cursor.execute (sql)


# 多条 tuple
# sql = " insert into users (name, age) values (%s, %s)" 
# val = ((" 李四" , 24) , (" 王五" , 25) , (" 洪六" , 26))
# cursor.executemany (sql, val)


# 批量插入 list
a=[" 李四" , 24]
sql = " insert into users (name, age) values (%s, %s)" 
lis_insert=[]
for i in range (500):
    lis_insert.append(a)
    if i%10000==0:
        cursor.executemany(sql,lis_insert)
        conn.commit()
        lis_insert=[]

#提交    
conn.commit()
#关闭    
conn.close()   
print "down"
