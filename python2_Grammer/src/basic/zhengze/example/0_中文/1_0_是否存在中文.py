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

sen=u"aa"
sen1=u"我的aa"


re_han = re.compile(ur"[\u4E00-\u9FA5]+") # 1.先编译正则表达式
lis=re_han.findall(sen)  # 开始使用findall
if lis !=[]:
    print "存在中文"
else:
    print "不存在"
    
print lis[0]




