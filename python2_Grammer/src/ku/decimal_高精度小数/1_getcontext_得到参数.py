#coding=utf-8
'''
Created on 2015年8月24日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

from decimal import getcontext



'''
获得当前的系统环境 所有的参数都在里面
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999999, 
Emax=999999999, capitals=1, flags=[], 
traps=[DivisionByZero, Overflow, InvalidOperation])

prec 参数为需要计算到小数点后多少位
'''
c = getcontext()
print c 



