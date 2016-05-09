#coding=utf-8
'''
Created on 2015年7月22日
@author: Administrator
'''
import traceback
try:  
    a=b  
    b=c  
except:  
    f=open("log.txt",'a')  # 创建log文件
    traceback.print_exc(file=f)  
    f.flush()  
    f.close()
