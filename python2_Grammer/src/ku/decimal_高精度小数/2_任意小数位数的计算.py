#coding=utf-8
'''
Created on 2015年8月24日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

from decimal import getcontext,Decimal




# 构造一个小数需要用字符串
con = getcontext()
b = Decimal('100.001111111111111111')
print b  # 100.001111111111111111 不存在丢失精度的问题


con.prec = 10 # 指定精度  指的是一共的经度100.0011111 有10个数字
print 'b:',b # 100.001111111111111111
print 'b+0:',b+0 # 100.00










