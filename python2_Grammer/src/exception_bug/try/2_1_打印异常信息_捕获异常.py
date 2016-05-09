#coding=utf-8
'''
Created on 2015年7月22日
@author: Administrator
'''
from __future__ import  division


    
try:   
    1/0
# 第一个表示捕获什么Exception
# 第二个参数表示异常的内容
except Exception,reason:  
    print Exception  
    print reason
finally:
    pass
    