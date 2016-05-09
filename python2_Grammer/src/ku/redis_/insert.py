# coding=utf-8
'''
尝试自己插入
Created on 2015年4月9日
@author: 李健博
'''
import redis
r = redis.Redis(host='10.95.130.184', port=6379, db=0)  # 如果设置了密码，就加上password=密码
r.flushdb()

url=r"C:\Users\Administrator\Desktop\new\123.txt"
f1=open(url,'r')
num=0
for  line in  f1.readlines(): 
    num=num+1
    if num>500:
        break
    try:
        b=line.split(r",")
#         print b[1]
        c=b[1].split(r"'")
        #中文
        zhongwen= c[1]
        print zhongwen
        #str 字符
#         print b[5]
        shuzi= float(b[5])
        print shuzi
        r[zhongwen] = shuzi
    except:    
        pass
    finally:
        pass
    
print "down"
        
