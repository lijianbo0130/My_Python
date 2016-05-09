#coding=utf-8
'''

'''
from __future__ import  division






# 双下划线 离开了类的定义就无法访问
class Double_Line():
    def __init__(self,age):
        self.__age = age
     
    def get_age(self):
        print self.__age
         


# 单下划线
class Sing_Line():
    def __init__(self,age):
        self._age = age
    
    def get_age(self):
        print self._age

def _my_single():
    print "mysingle" 
           
if __name__ == '__main__':
    '''
    单下划线" 开始的成员变量叫做保护变量，
    from single_line_double_line import * 的时候不会被引入
    但是如果from single_line_double_line import _my_single是可以访问的
    双下划线开头的变量在类定义以外的地方无法访问
    '''
    a=Sing_Line(3)# 可以访问 
    print a._age # 3
    b=Double_Line(4)
    print b.__age #异常无法访问__age
    #想要访问数据
    
        




