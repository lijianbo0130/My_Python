#coding=utf-8
'''
Created on 2015年6月23日
@author: Administrator
'''
a=[1,2,3,6,5,4]
# 把list变成 generator
b=iter(a)
print b
# 把generator 变成list
b=list(b)
print b[0]
