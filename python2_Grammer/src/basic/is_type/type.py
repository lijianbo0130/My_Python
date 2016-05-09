#coding=utf-8
'''
Created on 2016年3月29日
@author: 李健博
程序作用：

'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


x=int(5)
if type(x)==int: 
    print "x is interger. "
else: 
    print "false."
 
# 判断collection
x=[1]
if type(x)==list:
    print "x is list"
x={}
if type(x)==dict:
    print "x is dict"

x=(1,2)
if type(x)==tuple:
    print "x is tuple"

    
# 错误的方法 if都不会通过
if type(x)=="tuple":
    print "x is tuple"
    
if x is  tuple: 
    print x
    print "x is tuple"
    
