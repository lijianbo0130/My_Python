#coding=utf-8
'''
Created on 2015年6月15日
@author: Administrator
'''
class T():
    version="1.0"
    def __init__(self,a):
        self.a = a
    

t=T("a")

#打印类属性  dir  仅仅返回属性值列表
print dir(T) # ['__doc__', '__init__', '__module__', 'version']
print dir(t) # ['__doc__', '__init__', '__module__', 'a', 'version']

#打印属性  __dict  返回的key value dict
print T.__dict__ # {'__module__': '__main__', 'version': '1.0', '__doc__': None, '__init__': <function __init__ at 0x00000000022DADD8>}
print t.__dict__ # {'a': 'a'}



