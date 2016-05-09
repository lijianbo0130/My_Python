#coding=utf-8
'''
host:数据库主机名.默认是用本地主机 也可以使用ip
user:数据库登陆名.默认是当前用户
passwd:数据库登陆的秘密.默认为空
db:要使用的数据库名.没有默认值
charset:数据库编码
port=3309 端口
'''
import MySQLdb as db
#防止字符编码问题
import sys
reload(sys)   
sys.setdefaultencoding('utf-8')   # @UndefinedVariable

conn=db.connect(host="localhost",user="root",port=3309,
                    passwd="123456",db="data",charset="utf8")  

# 使用cursor()方法获取操作游标
cursor = conn.cursor() 
print cursor # 如果连接成功能打印出东西 <MySQLdb.cursors.Cursor object at 0x02575490>

#用cursor执行sql语句




# print connnect #连接成功 #<_mysql.connection open to 'localhost' at 21c1758>
conn.close() 