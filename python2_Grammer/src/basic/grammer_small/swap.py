#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''
a=5
b=10
print a,b
a, b = b, a
print a,b

a=[1,2,3]
a[0],a[1]=a[1],a[0]
print a