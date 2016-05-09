#coding=utf-8
'''
Created on 2015年4月15日
@author: Administrator
'''

#这个不会捕获到异常
try:
    l = ["a", "b"]
    int(l[2])
except ValueError, IndexError:  # To catch both exceptions, right?
    pass

#能捕获到异常
try:
    l = ["a", "b"]
    int(l[2])
except (ValueError, IndexError) as e:  
    print e