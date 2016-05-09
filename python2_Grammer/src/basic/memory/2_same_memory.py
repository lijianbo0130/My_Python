#coding=utf-8
'''
Created on 2016年3月28日
@author: 李健博
程序作用：
字符串和数字会被保存
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


# True
a = 1
b = 1
print(a is b)

# True
a = "good"
b = "good"
print(a is b)

# True
a = "very good morning"
b = "very good morning"
print(a is b)

# False
a = []
b = []
print(a is b)