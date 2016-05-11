#coding=utf-8
'''
Created on 2015年7月9日
@author: Administrator
很少单独使用
'''
'''
open
三种模式 都可以用 但是都不常用
readlines  全部读出来
readline
read
'''
f=open(r'data.txt','rb')
for  line in  f.readlines(): 
    print  line.strip()

