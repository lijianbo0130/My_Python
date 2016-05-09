#coding=utf-8
'''
单下划线作前缀，意思是只有类对象和子类对象自己能访问到这些变量，
且不能用'from module import *'导入。如：
'''

class Teacher():
    _name="sss"
    def __init__(self,name):
        self._name=name
        

t=Teacher("T")
print t._name
_name="wp"
names="ww"