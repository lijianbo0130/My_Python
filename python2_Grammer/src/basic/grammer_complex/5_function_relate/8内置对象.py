#coding=utf-8
'''
Created on 2015年4月17日
@author: Administrator
'''

def x():
    c=1
    return c

print x.__name__
x.count=1
x.count=x.count+1
print x.count
#显示函数内的对象
print dir(x)