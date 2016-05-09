#coding=utf-8
'''
Created on 2015年7月31日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


class Parent(object):  
    def __init__(self):  
        self.parent = 'parent.'  
        print 'Parent'  
      
    def bar(self,message):  
        print message, 'from Parent'  
          
class Child(Parent):  
    def __init__(self):  
        Parent.__init__(self)  
        print 'Child'  
          
    def bar(self,message):  
        Parent.bar(self,message)  
        print 'Child bar function.'  
        print self.parent  
          
if __name__=='__main__':  
    # 先新建一个父类的对象
    Child = Child()  
    Child.bar('HelloWorld') 