#coding=utf-8
'''
给成员变量赋值
'''
from __future__ import  division

class peo():
    s=[1,2,3,4,5]
    def __init__(self):
        self.name=0
        self.dd=self.s[self.name]


s=peo()
print s.dd

#直接调用会报异常
# print peo.age
# 初始化后可以调用
