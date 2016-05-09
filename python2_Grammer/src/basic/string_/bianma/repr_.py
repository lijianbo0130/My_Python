#coding=utf-8
'''
输出计算机里面保存的格式
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

a="我我"
print repr(a) #'\xe6\x88\x91\xe6\x88\x91'
