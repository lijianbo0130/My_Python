#coding=utf-8
'''
Created on 2015年8月14日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re

# 以s开头 以s结尾 ^和$和+ 修饰的都是s
lis=re.findall("^s+$", "s")
print lis  # ['s']

# 如果不使用+  只有s 能匹配中
lis=re.findall("^s$", "ss")# 目标字符串以s开头以S结尾
print lis  # ['s']




# lis=re.findall("^s*$", "s")# 目标字符串以s开头以S结尾
# print lis  # ['s']
# lis=re.findall("^s*$", "sss")# 目标字符串以s开头以S结尾
# print lis  # ['s']