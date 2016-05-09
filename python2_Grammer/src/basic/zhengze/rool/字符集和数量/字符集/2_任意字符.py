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
'''
.表示除了\n以外的任意字符
任意字符包括\n为 [\s\S]+
'''

# 普通查找
lis=re.findall(".+", "123651lop")
# print lis  # ['123651lop']

# 替换包括换行  [\s\S]*
s='''wdwdasdw
wdwdaadw'''

# 在[]中.失效
lis=re.findall("[.]", s)
print lis  # []

lis=re.findall("[\s\S]+", s) # 能够找到\n
print lis  # ['wdwdasdw\nwdwdaadw']

s='''wdwdasdw
wdwdaadw'''
# pt=re.compile(".+")
# lis=re.findall(pt, s)
# print lis  # ['123651lop']
