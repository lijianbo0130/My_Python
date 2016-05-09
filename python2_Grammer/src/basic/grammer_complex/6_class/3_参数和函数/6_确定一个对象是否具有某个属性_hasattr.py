#coding=utf-8
'''
Created on 2015年8月27日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
hasattr用于确定一个对象是否具有某个属性。

语法：
hasattr(object, name) -> bool
判断object中是否有name属性或者方法，返回一个布尔值。
'''

class Peo():
    s="123" # 静态变量
    def __init__(self,name):
        self.name = name
    
    def ss(self):
        print"a"

p=Peo("aaa")
print hasattr(p,"name") # True
print hasattr(p,"s") # True
print hasattr(p,"ss") # True