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

# ("^\d+$")
# re_han = re.compile(ur"[\u4E00-\u9FA5]+") # 1.先编译正则表达式
# lis=re_han.findall(sen1)  # 开始使用findall

sen=u"我的a"
pattern = re.compile(u"^[\u4E00-\u9FA5]+$") # 1.先编译正则表达式
lis=pattern.findall(sen) # 返回的是一个lis
print lis