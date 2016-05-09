#coding=utf-8
'''
Created on 2015年4月15日
@author: Administrator
当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值
args 为元组 kwargs 为字典
'''
def foo(*args,**kwargs):
    print 'args=',args
    print 'kwargs=',kwargs
    print '**********************'
    
if __name__=='__main__':
    foo(1,2,3)# args= (1, 2, 3) kwargs= {}
    foo(a=1,b=2,c=3)#  args= ()  kwargs= {'a': 1, 'c': 3, 'b': 2}
    foo(1,2,3,a=1,b=2,c=3)# args= (1, 2, 3)  kwargs= {'a': 1, 'c': 3, 'b': 2}
    foo(1,'b','c',a=1,b='b',c='c')