#coding=utf-8
'''
Created on 2016年3月28日
@author: 李健博
程序作用：
getrefcount(a) 查看有几个对象指向a所指向的内存
会比实际多一个
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a)) #2 

b = a
print(getrefcount(b))# 3