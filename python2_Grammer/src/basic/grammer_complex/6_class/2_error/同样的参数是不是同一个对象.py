#coding=utf-8
'''
Created on 2015年7月21日
@author: Administrator
'''
class Teacher():
    def __init__(self,name):
        self.name = name
        

t1=Teacher("a")
t2=Teacher("a")
t3=t1
print t1 is t3 # True
print t1 is t2 # False

set_t=set()
set_t.add(t1)
set_t.add(t2)
set_t.add(t3)
print set_t # 只有两个对象


