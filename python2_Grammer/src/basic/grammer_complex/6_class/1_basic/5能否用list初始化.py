#coding=utf-8
'''
用list会赋值给第一个变量
'''
from __future__ import  division


class Parent():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
        

a=(1,2)
b=Parent(a)#异常 需要两个变量
print b.n1
