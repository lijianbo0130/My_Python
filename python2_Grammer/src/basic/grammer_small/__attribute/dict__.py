#coding=utf-8
'''
Created on 2015年5月7日
@author: Administrator
'''

class T():
    def __init__(self,a):
        self.a = a

t=T(5)
t.f=5
#对象表示的是成员变量
print t.__dict__
d=T(5)
print d.__dict__
#类是类的属性
print T.__dict__