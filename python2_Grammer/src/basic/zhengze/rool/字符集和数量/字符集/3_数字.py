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

#单个数字  [0123456789] \d  
lis=re.findall("\d", "1d5d6f")
print lis  # ['1', '5', '6']

# 非数字 \D=[^\d]