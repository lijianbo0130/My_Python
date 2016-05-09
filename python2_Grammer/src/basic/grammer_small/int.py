#coding=utf-8
'''
Created on 2015年8月18日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

# 保留符号和整数位

b=-0.1
print int(b) # 0
b=0.1
print int(b) # 0
b=-0.7
print int(b) # 0
b=0.7
print int(b) # 0

# 关于字符串 python中字符串可以和数字比较大小 但是没哟任何意义
b="1"
print b>1
c=int(b) # 必须要这样转一下才能当数字用
print c,type(c)