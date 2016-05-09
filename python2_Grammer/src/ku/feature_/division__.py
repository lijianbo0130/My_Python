#coding=utf-8
'''
Created on 2016年3月21日
@author: 李健博
程序作用：
from __future__ import  division
如果不加这一条 
1/2=0
加了  
1/2=0.5
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


print 1/2
