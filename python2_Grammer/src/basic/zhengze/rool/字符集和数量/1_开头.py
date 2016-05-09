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

#^ 字符串的开头  多行匹配每一行的开头
# lis=re.findall("^s", "ssse")# 目标字符串以s开头
# print lis  # ['s']

# lis=re.findall("s", "ssse")# 
# print lis  # ['s', 's', 's']

# 以1开头 以1结尾  
lis=re.findall("^s$", "s")# 目标字符串以s开头以S结尾
print lis  # ['s']

