#coding=utf-8
'''
Created on 2015年8月5日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
'''
空格等符号都不是中文
'''
import re 
a=u"aa我来到北aa京清华大学     aa我来到北aa京清华大学"

pattern = re.compile(ur"[\u4E00-\u9FA5]+") # 1.先编译正则表达式
lis=pattern.findall(a) # 返回的是一个lis
for word in lis:
    print word