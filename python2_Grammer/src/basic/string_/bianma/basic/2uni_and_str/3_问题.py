#coding=utf-8
'''
Created on 2015年7月2日
@author: Administrator
'''

'''
把str和unicode比较会出异常不要做这样的事
'''
# a="我"
# b=u"我"
# if a==b: print True # "a"和u"a" 如果比较就会出异常
# if a in b: print a # in 也会异常
