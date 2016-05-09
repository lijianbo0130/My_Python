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

#$ 字符串的结尾  多行匹配每一行的结尾
lis=re.findall("se$", "ssse")# 以se结尾
print lis  # ['se']