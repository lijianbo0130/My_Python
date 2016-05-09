#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''



import json;    
import urllib2  
#得到json文件
page=urllib2.urlopen("http://10.95.136.184:8080/yuqingService/webservice/y/context/getContextList?lastId=0").read() 
#解析
jsonVal = json.loads(page)  
#返回一个list  
print   type(jsonVal)
for i in jsonVal:
    #list  里面装有多个dict
    print   type(i)  
   
        


