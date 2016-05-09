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

# ^表示取反 在[]中才表示取反
lis=re.findall("[^abc]", "abd") #^表示取反 [^abc]表示不是abc的任何字符
print lis # ['d']
