#coding=utf-8
'''
Created on 2015年5月25日
@author: Administrator
'''
import MySQLdb  
  
conn = MySQLdb.connect (host = "172.17.23.121", user = "fkong", passwd = "fkong", db = "fkong")  
cursor = conn.cursor ()  

#得到 所有数据
cursor.execute ("SELECT * FROM TEST")  
rows = cursor.fetchall()  
# 每一个 row是一个tuple 表示一行数据 row1=(name1,age1) 

# 如果select 回来是0 可以用有多少行来判断
# 输出有多少行  
print "Number of rows returned: %d" % cursor.rowcount 


# 读取回来的数据是包含数据类型的 (8841188L,u"aaaa") 如果读取了一个int 是不能当作str使用



# 得到所有数据
cursor.execute('select account_name from account')  
for row in cursor.fetchall():  
    print row[0]   



#得到一个数据  
cursor.execute ("SELECT * FROM TEST")  
while (True):  
    row = cursor.fetchone()  
    if row == None:  
        break  
    print "%d, %s, %s, %s" % (row[0], row[1], row[2], row[3])  
      
print "Number of rows returned: %d" % cursor.rowcount  

#得到单个数据  
cursor.execute("SELECT VERSION()")
#取得上个查询的结果，是单个结果
data = cursor.fetchone()
#不这样写会有bug
Max_num = cursor.fetchone()[0]


  
cursor.close ()  
conn.close () 