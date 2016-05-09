#coding=utf-8
'''
Created on 2016年3月23日
@author: 李健博
程序作用：
识别这种 0851-1561GZ14CL53
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re
#判断s是否由纯数字组成
s1=u"2016-HJ91100-1003  三"
s2=u"123ss45678"


# 正则表达式
pattern=re.compile(ur"[0-9a-zA-Z]+[-]+[0-9a-zA-Z-]*[0-9a-zA-Z-]")
lis=pattern.findall(s1) # 返回的是一个lis
print lis
