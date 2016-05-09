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

# ? 出现0次或者1次
lis=re.findall("1s?", "1s16")
print lis  # ['1s', '1']