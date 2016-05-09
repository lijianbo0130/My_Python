#coding=utf-8
'''
Created on 2015年8月27日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

class A:   
    def __init__(self):   
        self.name = 'zhangjing'  
    #self.age='24'
    def method(self):   
        print"method print"  
  
Instance = A()   
print getattr(Instance , 'name', "not find") #如果Instance 对象中有属性name则打印self.name的值，否则打印'not find'
print getattr(Instance , 'age', 'not find')   #如果Instance 对象中有属性age则打印self.age的值，否则打印'not find'

print getattr(Instance, 'method', 'default')   
#如果有方法method，否则打印其地址，否则打印default   
print getattr(Instance, 'method', 'default')()   
#如果有方法method，运行函数并打印None否则打印default 