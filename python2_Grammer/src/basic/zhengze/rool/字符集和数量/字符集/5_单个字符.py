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
# 单个字母 \w [A-Za-z0-9_] 包含 '_'
# 非单词字符 \W


lis=re.findall("\w", "_ppa")#\w 包含_
print lis  # ['_', 'p', 'p', 'a']