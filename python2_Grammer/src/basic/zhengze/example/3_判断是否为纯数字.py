#coding=utf-8
'''
Created on 2015年8月5日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re

#判断s是否由纯数字组成
s1="12345678"
s2="123ss45678"
s3="1a"
# ^[A-Za-z]+$
# 正则表达式
pattern=re.compile("^\d+$")
lis=pattern.findall(s3) # 返回的是一个lis


if lis !=[]:
    print "是纯数字"
else:
    print "不是纯数字"