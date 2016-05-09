#coding=utf-8
'''
Created on 2016年3月23日
@author: 李健博
程序作用：

'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
空表示的是""
用if可以直接判断
'''

if (""):# 不会进入if
    print "a"
else:
    print "b"# b
    
if ("aa"): # 会进入if
    print "aa"# aa
else:
    print "b"
    
if (1): # 会进入if
    print "a"

if (0): # 不会进入if
    print "a"