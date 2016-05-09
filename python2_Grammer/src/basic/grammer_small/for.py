#coding=utf-8
'''
Created on 2015年8月21日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
for循环中无法改变列表中的值
'''
a=[1,2,3]
for b in a:
    b=5

print a