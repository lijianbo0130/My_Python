#coding=utf-8
'''
Created on 2015年8月4日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re

# +表示一个或者多个
lis=re.findall("\d+", "1s111s6")
print lis  # ['1', '111', '6']