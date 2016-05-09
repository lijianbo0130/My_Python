# coding=utf-8
'''
最简单的测试脚本
Created on 2015年4月9日
@author: 李健博
'''
import redis
r = redis.Redis(host='10.95.130.184', port=6379, db=0)  # 如果设置了密码，就加上password=密码

def devide(str1):
    v_list=[]
    r_list=[]
    for i in  r.keys():
        v_list.append(i)
    
    for word in v_list:
        if word in str1:
            r_list.append(word)
    return r_list
    